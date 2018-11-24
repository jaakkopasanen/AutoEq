# Grado SR325e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.4; 37 4.7; 41 3.8; 45 3.0; 49 2.4; 54 1.8; 60 1.3; 66 0.9; 72 0.7; 79 0.6; 87 0.4; 96 0.3; 106 0.1; 116 -0.1; 128 -0.2; 141 -0.2; 155 -0.2; 170 -0.2; 187 -0.2; 206 0.1; 227 0.2; 249 0.2; 274 -0.1; 302 0.1; 332 0.4; 365 0.6; 402 0.6; 442 0.6; 486 0.5; 535 0.5; 588 0.6; 647 0.7; 712 0.7; 783 0.4; 861 0.2; 947 0.0; 1042 0.1; 1146 0.1; 1261 -0.2; 1387 -1.1; 1526 -2.1; 1678 -3.4; 1846 -5.9; 2031 -8.6; 2234 -8.4; 2457 -6.5; 2703 -4.5; 2973 -2.6; 3270 -1.3; 3597 -0.2; 3957 -1.7; 4353 -4.0; 4788 -1.0; 5267 0.0; 5793 0.5; 6373 2.0; 7010 1.8; 7711 -1.2; 8482 -6.4; 9330 -10.3; 10263 -9.3; 11289 -4.0; 12418 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR325e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 1.08 | 6.6 dB   |
| Peaking | 2048 Hz  | 3.36 | -7.1 dB  |
| Peaking | 2434 Hz  | 2.8  | -3.7 dB  |
| Peaking | 6872 Hz  | 3.82 | 4.4 dB   |
| Peaking | 9557 Hz  | 3.07 | -11.9 dB |
| Peaking | 647 Hz   | 1.06 | 0.8 dB   |
| Peaking | 3613 Hz  | 6.05 | 1.8 dB   |
| Peaking | 4406 Hz  | 4.62 | -4.5 dB  |
| Peaking | 4956 Hz  | 6.03 | 2.5 dB   |
| Peaking | 12752 Hz | 5.05 | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Grado%20SR325e/Grado%20SR325e.png)