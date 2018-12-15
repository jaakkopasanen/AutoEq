# Kennerton Magister

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.8; 49 5.4; 54 4.9; 60 4.8; 66 5.1; 72 5.3; 79 3.5; 87 1.1; 96 0.6; 106 -1.2; 116 -2.6; 128 -3.6; 141 -4.4; 155 -4.8; 170 -4.9; 187 -4.8; 206 -4.9; 227 -3.8; 249 -1.8; 274 1.0; 302 4.5; 332 6.0; 365 5.9; 402 3.6; 442 1.7; 486 1.1; 535 0.1; 588 -0.5; 647 -0.5; 712 -0.1; 783 0.4; 861 0.4; 947 0.2; 1042 0.2; 1146 0.6; 1261 1.2; 1387 1.9; 1526 2.6; 1678 3.3; 1846 3.6; 2031 4.0; 2234 3.9; 2457 2.7; 2703 1.4; 2973 0.6; 3270 0.3; 3597 4.8; 3957 1.2; 4353 -1.1; 4788 -4.2; 5267 -6.7; 5793 -5.9; 6373 3.9; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -3.1; 15026 -7.5; 16529 -8.9; 18182 -6.3; 20000 -1.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kennerton Magister GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kennerton Magister ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 43 Hz    | 0.34 | 7.2 dB   |
| Peaking | 164 Hz   | 0.85 | -9.2 dB  |
| Peaking | 337 Hz   | 2.45 | 9.1 dB   |
| Peaking | 5315 Hz  | 7.36 | -7.9 dB  |
| Peaking | 16614 Hz | 1.88 | -10.1 dB |
| Peaking | 2002 Hz  | 1.11 | 7.3 dB   |
| Peaking | 3726 Hz  | 7.14 | 6.8 dB   |
| Peaking | 5843 Hz  | 0.22 | -4.8 dB  |
| Peaking | 6616 Hz  | 7.27 | 7.3 dB   |
| Peaking | 10425 Hz | 0.8  | 5.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Kennerton%20Magister/Kennerton%20Magister.png)