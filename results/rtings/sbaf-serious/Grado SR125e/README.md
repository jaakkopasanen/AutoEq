# Grado SR125e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.6; 34 4.9; 37 4.1; 41 3.3; 45 2.6; 49 2.0; 54 1.4; 60 0.9; 66 0.6; 72 0.4; 79 0.3; 87 0.1; 96 -0.0; 106 -0.2; 116 -0.4; 128 -0.5; 141 -0.6; 155 -0.6; 170 -0.6; 187 -0.5; 206 -0.3; 227 -0.0; 249 0.2; 274 0.3; 302 -0.0; 332 0.0; 365 0.2; 402 0.3; 442 0.3; 486 0.4; 535 0.4; 588 0.5; 647 0.5; 712 0.5; 783 0.3; 861 0.1; 947 0.0; 1042 0.1; 1146 0.1; 1261 -0.2; 1387 -1.0; 1526 -2.2; 1678 -3.5; 1846 -7.1; 2031 -9.1; 2234 -8.1; 2457 -6.5; 2703 -4.8; 2973 -2.7; 3270 -1.2; 3597 -1.3; 3957 -4.6; 4353 -3.0; 4788 1.0; 5267 -0.9; 5793 -1.1; 6373 -1.7; 7010 -4.4; 7711 -5.5; 8482 -8.8; 9330 -10.7; 10263 -5.7; 11289 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR125e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 1.05 | 6.5 dB   |
| Peaking | 124 Hz   | 1.42 | -0.9 dB  |
| Peaking | 2008 Hz  | 3.7  | -7.4 dB  |
| Peaking | 2432 Hz  | 2.41 | -4.1 dB  |
| Peaking | 8961 Hz  | 3.17 | -11.2 dB |
| Peaking | 695 Hz   | 0.9  | 0.6 dB   |
| Peaking | 4117 Hz  | 5.58 | -7.1 dB  |
| Peaking | 4368 Hz  | 2.28 | 3.3 dB   |
| Peaking | 7023 Hz  | 5.4  | -1.9 dB  |
| Peaking | 11592 Hz | 5.52 | 2.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Grado%20SR125e/Grado%20SR125e.png)