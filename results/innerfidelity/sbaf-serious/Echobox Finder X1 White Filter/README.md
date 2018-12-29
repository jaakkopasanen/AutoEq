# Echobox Finder X1 White Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 21 -10.4; 23 -10.4; 25 -10.3; 28 -10.3; 31 -10.2; 34 -10.0; 37 -9.9; 41 -9.8; 45 -9.6; 49 -9.5; 54 -9.3; 60 -9.2; 66 -9.0; 72 -8.9; 79 -8.8; 87 -8.7; 96 -8.6; 106 -8.3; 116 -8.0; 128 -7.7; 141 -7.4; 155 -7.1; 170 -6.7; 187 -6.2; 206 -5.7; 227 -5.2; 249 -4.7; 274 -4.2; 302 -3.6; 332 -3.1; 365 -2.5; 402 -2.0; 442 -1.4; 486 -1.0; 535 -0.5; 588 0.1; 647 0.4; 712 0.6; 783 0.8; 861 0.6; 947 0.3; 1042 -0.1; 1146 -0.5; 1261 -1.0; 1387 -1.6; 1526 -2.3; 1678 -2.8; 1846 -3.0; 2031 -2.9; 2234 -3.0; 2457 -2.8; 2703 -3.0; 2973 -3.3; 3270 -3.8; 3597 -4.4; 3957 -5.3; 4353 -7.1; 4788 -7.9; 5267 -8.0; 5793 -8.1; 6373 -8.6; 7010 -6.6; 7711 -4.7; 8482 -3.6; 9330 -4.1; 10263 -6.6; 11289 -6.5; 12418 -2.8; 13660 -2.4; 15026 -4.1; 16529 -0.7; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Echobox Finder X1 White Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Echobox Finder X1 White Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.21 | -10.2 dB |
| Peaking | 159 Hz   | 0.79 | -3.4 dB  |
| Peaking | 1869 Hz  | 2.5  | -2.2 dB  |
| Peaking | 5424 Hz  | 1.1  | -8.4 dB  |
| Peaking | 10982 Hz | 3.11 | -5.5 dB  |
| Peaking | 314 Hz   | 2.23 | -0.7 dB  |
| Peaking | 750 Hz   | 1.51 | 1.6 dB   |
| Peaking | 1463 Hz  | 3.52 | -0.7 dB  |
| Peaking | 8534 Hz  | 7.06 | 1.2 dB   |
| Peaking | 15051 Hz | 5.32 | -3.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Echobox%20Finder%20X1%20White%20Filter/Echobox%20Finder%20X1%20White%20Filter.png)