# Focal Elear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.5; 79 4.9; 87 4.2; 96 3.5; 106 2.7; 116 1.9; 128 1.2; 141 0.6; 155 0.1; 170 -0.4; 187 -0.7; 206 -0.9; 227 -0.9; 249 -0.8; 274 -0.6; 302 -0.3; 332 -0.0; 365 0.2; 402 0.4; 442 0.4; 486 0.4; 535 0.3; 588 0.3; 647 0.5; 712 0.4; 783 0.2; 861 -0.0; 947 -0.0; 1042 0.0; 1146 -0.0; 1261 -0.2; 1387 -0.0; 1526 -0.1; 1678 0.8; 1846 2.4; 2031 4.0; 2234 4.4; 2457 3.8; 2703 3.4; 2973 3.2; 3270 3.6; 3597 4.2; 3957 5.9; 4353 6.0; 4788 6.0; 5267 4.7; 5793 0.7; 6373 4.9; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.2; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 0.23 | 6.9 dB  |
| Peaking | 170 Hz   | 0.8  | -5.1 dB |
| Peaking | 2214 Hz  | 3.4  | 3.9 dB  |
| Peaking | 4367 Hz  | 1.68 | 6.2 dB  |
| Peaking | 24000 Hz | 2.2  | 1.7 dB  |
| Peaking | 1387 Hz  | 3.15 | -0.9 dB |
| Peaking | 5732 Hz  | 9.14 | -4.9 dB |
| Peaking | 6442 Hz  | 3.22 | 5.0 dB  |
| Peaking | 7512 Hz  | 3.92 | -0.7 dB |
| Peaking | 7709 Hz  | 1.88 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Elear/Focal%20Elear.png)