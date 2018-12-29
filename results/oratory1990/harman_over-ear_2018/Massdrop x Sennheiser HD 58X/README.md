# Massdrop x Sennheiser HD 58X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.5; 28 4.9; 31 4.4; 34 4.1; 37 3.7; 41 3.2; 45 2.8; 49 2.6; 54 2.4; 60 2.0; 66 2.2; 72 2.5; 79 1.0; 87 0.2; 96 -0.3; 106 -0.7; 116 -1.0; 128 -1.3; 141 -1.6; 155 -1.7; 170 -1.6; 187 -1.7; 206 -1.7; 227 -1.6; 249 -1.5; 274 -1.3; 302 -1.1; 332 -0.7; 365 -0.4; 402 -0.2; 442 0.0; 486 0.1; 535 0.3; 588 0.6; 647 0.6; 712 0.5; 783 0.5; 861 0.6; 947 0.6; 1042 -0.3; 1146 -0.6; 1261 -0.3; 1387 0.2; 1526 1.0; 1678 1.7; 1846 2.7; 2031 3.6; 2234 4.0; 2457 4.3; 2703 3.7; 2973 2.7; 3270 1.8; 3597 1.6; 3957 2.3; 4353 4.0; 4788 1.9; 5267 -1.7; 5793 -0.7; 6373 4.7; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -2.0; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Sennheiser HD 58X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Sennheiser HD 58X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.28 | 6.0 dB  |
| Peaking | 55 Hz   | 2.63 | 1.8 dB  |
| Peaking | 2366 Hz | 2.08 | 4.6 dB  |
| Peaking | 4361 Hz | 8.2  | 3.9 dB  |
| Peaking | 6579 Hz | 9.87 | 5.1 dB  |
| Peaking | 37 Hz   | 3.25 | 0.9 dB  |
| Peaking | 73 Hz   | 5.61 | 1.9 dB  |
| Peaking | 175 Hz  | 0.7  | -1.9 dB |
| Peaking | 591 Hz  | 1.92 | 0.9 dB  |
| Peaking | 5416 Hz | 9.6  | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Sennheiser%20HD%2058X/Massdrop%20x%20Sennheiser%20HD%2058X.png)