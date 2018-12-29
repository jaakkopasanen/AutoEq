# Ultrasone Edition 10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.6; 34 4.8; 37 4.1; 41 3.3; 45 2.8; 49 2.5; 54 2.0; 60 1.2; 66 0.8; 72 0.3; 79 0.1; 87 -0.2; 96 -0.6; 106 -0.9; 116 -0.8; 128 -0.9; 141 -0.9; 155 -0.8; 170 -0.5; 187 -0.4; 206 -0.1; 227 0.2; 249 0.4; 274 0.7; 302 0.8; 332 1.1; 365 1.3; 402 1.5; 442 1.7; 486 1.6; 535 1.6; 588 1.6; 647 1.5; 712 1.4; 783 1.4; 861 0.8; 947 0.3; 1042 -0.3; 1146 -0.9; 1261 -1.3; 1387 -1.0; 1526 -0.0; 1678 1.6; 1846 5.8; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 4.2; 3270 0.7; 3597 -2.1; 3957 -4.1; 4353 -3.6; 4788 1.5; 5267 0.9; 5793 -5.1; 6373 -9.9; 7010 -1.7; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -3.6; 15026 -8.2; 16529 -6.3; 18182 -1.1; 20000 -0.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Edition 10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 1.24 | 6.6 dB   |
| Peaking | 2400 Hz  | 1.89 | 7.2 dB   |
| Peaking | 3918 Hz  | 5.08 | -6.1 dB  |
| Peaking | 6283 Hz  | 8.44 | -11.2 dB |
| Peaking | 15556 Hz | 2.86 | -9.4 dB  |
| Peaking | 135 Hz   | 1.22 | -1.5 dB  |
| Peaking | 736 Hz   | 0.49 | 2.4 dB   |
| Peaking | 1338 Hz  | 1.2  | -4.2 dB  |
| Peaking | 1867 Hz  | 6.5  | 3.9 dB   |
| Peaking | 9446 Hz  | 1.09 | 0.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20Edition%2010/Ultrasone%20Edition%2010.png)