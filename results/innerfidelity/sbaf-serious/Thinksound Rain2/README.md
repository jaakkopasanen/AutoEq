# Thinksound Rain2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -8.7; 23 -8.8; 25 -8.9; 28 -9.0; 31 -9.1; 34 -9.2; 37 -9.3; 41 -9.4; 45 -9.5; 49 -9.7; 54 -9.9; 60 -10.1; 66 -10.3; 72 -10.5; 79 -10.8; 87 -11.0; 96 -11.3; 106 -11.3; 116 -11.3; 128 -11.4; 141 -11.3; 155 -11.2; 170 -11.0; 187 -10.7; 206 -10.4; 227 -9.9; 249 -9.4; 274 -8.8; 302 -8.2; 332 -7.6; 365 -6.9; 402 -6.2; 442 -5.3; 486 -4.7; 535 -3.9; 588 -2.9; 647 -2.1; 712 -1.7; 783 -0.8; 861 -0.5; 947 -0.1; 1042 0.1; 1146 0.4; 1261 0.6; 1387 0.2; 1526 -0.6; 1678 -1.1; 1846 -1.0; 2031 -0.5; 2234 0.1; 2457 1.1; 2703 1.6; 2973 2.2; 3270 2.6; 3597 2.1; 3957 0.7; 4353 -2.1; 4788 -3.9; 5267 -6.2; 5793 -10.6; 6373 -7.9; 7010 -2.9; 7711 0.1; 8482 0.0; 9330 -0.4; 10263 -2.5; 11289 -0.5; 12418 0.0; 13660 0.0; 15026 -0.0; 16529 -2.5; 18182 -0.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Thinksound Rain2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound Rain2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.22 | -8.5 dB  |
| Peaking | 155 Hz   | 0.64 | -6.3 dB  |
| Peaking | 332 Hz   | 1.17 | -3.3 dB  |
| Peaking | 3256 Hz  | 2.75 | 3.5 dB   |
| Peaking | 5828 Hz  | 3.71 | -11.4 dB |
| Peaking | 1178 Hz  | 1.92 | 1.4 dB   |
| Peaking | 1725 Hz  | 3.6  | -1.5 dB  |
| Peaking | 7896 Hz  | 5.52 | 2.1 dB   |
| Peaking | 10343 Hz | 8.41 | -2.5 dB  |
| Peaking | 16865 Hz | 4.34 | -2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thinksound%20Rain2/Thinksound%20Rain2.png)