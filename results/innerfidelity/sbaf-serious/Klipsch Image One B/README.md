# Klipsch Image One B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.4dB
GraphicEQ: 21 -9.6; 23 -9.8; 25 -10.0; 28 -10.1; 31 -10.3; 34 -10.3; 37 -10.4; 41 -10.4; 45 -10.4; 49 -10.4; 54 -10.4; 60 -10.5; 66 -10.5; 72 -10.5; 79 -10.6; 87 -10.7; 96 -10.8; 106 -10.4; 116 -10.1; 128 -10.2; 141 -10.4; 155 -10.3; 170 -9.8; 187 -9.8; 206 -9.4; 227 -9.0; 249 -8.6; 274 -8.2; 302 -7.5; 332 -6.5; 365 -5.1; 402 -3.7; 442 -2.0; 486 -1.1; 535 -0.2; 588 0.7; 647 1.2; 712 1.8; 783 1.9; 861 0.9; 947 -0.1; 1042 -0.0; 1146 -1.3; 1261 -2.2; 1387 -3.0; 1526 -3.7; 1678 -4.6; 1846 -5.3; 2031 -5.9; 2234 -6.3; 2457 -6.9; 2703 -7.7; 2973 -7.5; 3270 -6.2; 3597 -4.2; 3957 -1.8; 4353 -0.5; 4788 1.2; 5267 -0.2; 5793 -0.4; 6373 1.3; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.3; 11289 -0.2; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image One B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image One B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.23 | -9.6 dB  |
| Peaking | 268 Hz  | 0.41 | -8.2 dB  |
| Peaking | 639 Hz  | 0.79 | 8.0 dB   |
| Peaking | 2981 Hz | 0.75 | -12.9 dB |
| Peaking | 4413 Hz | 0.84 | 8.4 dB   |
| Peaking | 4926 Hz | 5.53 | 1.9 dB   |
| Peaking | 5492 Hz | 6.23 | -2.1 dB  |
| Peaking | 6084 Hz | 3.38 | -1.2 dB  |
| Peaking | 6815 Hz | 7.19 | 3.9 dB   |
| Peaking | 8507 Hz | 1.34 | -0.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Image%20One%20B/Klipsch%20Image%20One%20B.png)