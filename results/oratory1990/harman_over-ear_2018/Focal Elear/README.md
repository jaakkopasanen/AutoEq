# Focal Elear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.7; 25 3.3; 28 3.0; 31 2.8; 34 2.6; 37 2.4; 41 2.2; 45 2.1; 49 1.9; 54 1.8; 60 1.6; 66 1.4; 72 1.1; 79 0.8; 87 0.5; 96 0.1; 106 -0.2; 116 -0.5; 128 -0.7; 141 -0.8; 155 -0.9; 170 -1.0; 187 -1.0; 206 -1.0; 227 -0.9; 249 -0.8; 274 -0.6; 302 -0.3; 332 -0.0; 365 0.2; 402 0.4; 442 0.4; 486 0.4; 535 0.3; 588 0.3; 647 0.5; 712 0.4; 783 0.2; 861 -0.0; 947 -0.0; 1042 0.0; 1146 -0.0; 1261 -0.2; 1387 -0.0; 1526 -0.1; 1678 0.8; 1846 2.4; 2031 4.0; 2234 4.4; 2457 3.8; 2703 3.4; 2973 3.2; 3270 3.6; 3597 4.2; 3957 5.9; 4353 6.0; 4788 6.0; 5267 4.7; 5793 0.7; 6373 4.9; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.2; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 22 Hz    |  1.2  | 3.9 dB  |
| Peaking | 51 Hz    |  2.18 | 1.5 dB  |
| Peaking | 2212 Hz  |  3.39 | 3.9 dB  |
| Peaking | 4366 Hz  |  1.67 | 6.2 dB  |
| Peaking | 24000 Hz |  2.2  | 1.7 dB  |
| Peaking | 177 Hz   |  1.64 | -1.3 dB |
| Peaking | 1455 Hz  |  4.41 | -0.9 dB |
| Peaking | 5737 Hz  | 12.67 | -3.2 dB |
| Peaking | 6496 Hz  | 10.31 | 3.6 dB  |
| Peaking | 19918 Hz |  3.39 | -7.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Elear/Focal%20Elear.png)