# Jabra Elite 25e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 21 -7.1; 23 -7.4; 25 -7.6; 28 -7.9; 31 -8.1; 34 -8.2; 37 -8.2; 41 -8.3; 45 -8.3; 49 -8.3; 54 -8.3; 60 -8.5; 66 -8.5; 72 -8.4; 79 -8.4; 87 -8.4; 96 -8.6; 106 -8.8; 116 -9.1; 128 -9.3; 141 -9.4; 155 -9.3; 170 -9.2; 187 -9.0; 206 -9.0; 227 -8.7; 249 -8.1; 274 -7.4; 302 -6.5; 332 -5.7; 365 -4.9; 402 -4.1; 442 -3.2; 486 -2.3; 535 -1.4; 588 -0.6; 647 0.3; 712 0.9; 783 1.0; 861 0.6; 947 0.4; 1042 -0.3; 1146 -0.9; 1261 -1.3; 1387 -1.7; 1526 -2.1; 1678 -2.2; 1846 -1.9; 2031 -1.6; 2234 -1.0; 2457 -0.6; 2703 -0.2; 2973 0.5; 3270 2.3; 3597 3.5; 3957 2.3; 4353 0.2; 4788 0.4; 5267 1.9; 5793 4.4; 6373 3.8; 7010 2.5; 7711 -0.3; 8482 -2.1; 9330 -0.1; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.1; 16529 -2.5; 18182 -3.5; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 25e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 25e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.3  | -7.9 dB |
| Peaking | 152 Hz   | 0.92 | -4.9 dB |
| Peaking | 266 Hz   | 1.37 | -4.2 dB |
| Peaking | 3597 Hz  | 6.38 | 3.8 dB  |
| Peaking | 6072 Hz  | 4.96 | 5.0 dB  |
| Peaking | 423 Hz   | 3.34 | -0.9 dB |
| Peaking | 750 Hz   | 1.94 | 2.2 dB  |
| Peaking | 1629 Hz  | 1.79 | -2.4 dB |
| Peaking | 17239 Hz | 3.31 | -1.6 dB |
| Peaking | 19645 Hz | 1.39 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Jabra%20Elite%2025e/Jabra%20Elite%2025e.png)