# Jabra Elite 25e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.8dB
GraphicEQ: 21 -7.5; 23 -7.7; 25 -7.9; 28 -8.0; 31 -8.1; 34 -8.1; 37 -8.1; 41 -8.1; 45 -8.0; 49 -8.0; 54 -8.0; 60 -8.2; 66 -8.3; 72 -8.4; 79 -8.5; 87 -8.8; 96 -9.0; 106 -9.3; 116 -9.6; 128 -9.8; 141 -9.9; 155 -9.9; 170 -9.8; 187 -9.6; 206 -9.5; 227 -9.2; 249 -8.7; 274 -8.0; 302 -7.3; 332 -6.6; 365 -5.9; 402 -5.2; 442 -4.4; 486 -3.5; 535 -2.6; 588 -1.7; 647 -0.8; 712 0.1; 783 0.5; 861 0.4; 947 0.4; 1042 -0.3; 1146 -1.1; 1261 -1.5; 1387 -1.7; 1526 -1.7; 1678 -1.8; 1846 -2.0; 2031 -2.0; 2234 -1.5; 2457 -1.1; 2703 -1.0; 2973 -1.1; 3270 -0.3; 3597 0.3; 3957 -0.1; 4353 -1.1; 4788 -1.3; 5267 -1.1; 5793 0.5; 6373 0.1; 7010 -0.4; 7711 -2.7; 8482 -3.1; 9330 -0.1; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.1; 15026 -5.5; 16529 -8.9; 18182 -11.1; 20000 -12.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 25e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-7**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 25e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.19 | -7.7 dB  |
| Peaking | 207 Hz   | 0.75 | -6.2 dB  |
| Peaking | 1897 Hz  | 2.19 | -1.9 dB  |
| Peaking | 8110 Hz  | 9    | -3.3 dB  |
| Peaking | 18885 Hz | 1.16 | -13.4 dB |
| Peaking | 414 Hz   | 1.89 | -1.1 dB  |
| Peaking | 804 Hz   | 1.66 | 2.2 dB   |
| Peaking | 1283 Hz  | 2.64 | -1.2 dB  |
| Peaking | 13517 Hz | 1.74 | 3.8 dB   |
| Peaking | 15652 Hz | 2.47 | -4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%2025e/Jabra%20Elite%2025e.png)