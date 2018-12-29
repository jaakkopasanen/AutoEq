# Echobox Finder X1 Black Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.8dB
GraphicEQ: 21 -10.7; 23 -10.7; 25 -10.7; 28 -10.6; 31 -10.5; 34 -10.4; 37 -10.2; 41 -10.1; 45 -9.9; 49 -9.8; 54 -9.6; 60 -9.4; 66 -9.3; 72 -9.2; 79 -9.1; 87 -9.0; 96 -8.8; 106 -8.6; 116 -8.2; 128 -8.0; 141 -7.7; 155 -7.3; 170 -6.9; 187 -6.5; 206 -6.0; 227 -5.4; 249 -4.9; 274 -4.4; 302 -3.8; 332 -3.3; 365 -2.7; 402 -2.2; 442 -1.6; 486 -1.2; 535 -0.7; 588 -0.1; 647 0.3; 712 0.3; 783 0.7; 861 0.5; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -1.0; 1387 -1.6; 1526 -2.3; 1678 -2.9; 1846 -3.1; 2031 -3.2; 2234 -3.4; 2457 -3.5; 2703 -4.0; 2973 -4.7; 3270 -5.3; 3597 -5.5; 3957 -6.0; 4353 -7.8; 4788 -9.0; 5267 -9.8; 5793 -11.1; 6373 -11.4; 7010 -8.6; 7711 -7.2; 8482 -7.9; 9330 -9.7; 10263 -8.6; 11289 -2.5; 12418 0.0; 13660 -2.1; 15026 -4.5; 16529 -0.5; 18182 0.0; 20000 -0.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Echobox Finder X1 Black Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-7**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Echobox Finder X1 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.21 | -10.5 dB |
| Peaking | 162 Hz   | 0.78 | -3.5 dB  |
| Peaking | 5667 Hz  | 0.84 | -10.4 dB |
| Peaking | 9674 Hz  | 5.3  | -5.9 dB  |
| Peaking | 24000 Hz | 2.01 | -1.4 dB  |
| Peaking | 799 Hz   | 1.72 | 1.7 dB   |
| Peaking | 1794 Hz  | 1.73 | -1.5 dB  |
| Peaking | 3939 Hz  | 5.68 | 1.2 dB   |
| Peaking | 12367 Hz | 5    | 3.7 dB   |
| Peaking | 14870 Hz | 4.97 | -4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Echobox%20Finder%20X1%20Black%20Filter/Echobox%20Finder%20X1%20Black%20Filter.png)