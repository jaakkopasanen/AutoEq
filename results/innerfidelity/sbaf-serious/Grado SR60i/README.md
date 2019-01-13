# Grado SR60i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.7; 34 5.0; 37 4.2; 41 3.2; 45 2.4; 49 1.6; 54 0.8; 60 0.1; 66 -0.4; 72 -0.9; 79 -1.2; 87 -1.7; 96 -2.1; 106 -2.1; 116 -2.2; 128 -2.3; 141 -2.3; 155 -2.3; 170 -2.1; 187 -1.9; 206 -1.8; 227 -1.3; 249 -1.1; 274 -1.0; 302 -0.8; 332 -0.8; 365 -0.6; 402 -0.4; 442 -0.2; 486 -0.2; 535 -0.1; 588 0.3; 647 0.4; 712 0.2; 783 0.4; 861 0.2; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.7; 1387 -1.5; 1526 -2.6; 1678 -3.4; 1846 -6.2; 2031 -9.8; 2234 -8.1; 2457 -5.1; 2703 -2.9; 2973 -1.2; 3270 -1.5; 3597 -1.1; 3957 1.3; 4353 1.5; 4788 2.1; 5267 0.5; 5793 1.4; 6373 2.4; 7010 -1.3; 7711 -1.5; 8482 -1.7; 9330 -1.1; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR60i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.73 | 6.9 dB   |
| Peaking | 105 Hz  | 0.51 | -3.1 dB  |
| Peaking | 2096 Hz | 2.09 | -11.7 dB |
| Peaking | 2989 Hz | 0.32 | 2.5 dB   |
| Peaking | 8256 Hz | 2.64 | -3.2 dB  |
| Peaking | 2899 Hz | 3.3  | 0.7 dB   |
| Peaking | 3517 Hz | 3.91 | -3.0 dB  |
| Peaking | 4005 Hz | 3.02 | 1.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR60i/Grado%20SR60i.png)