# Jabra Elite 65t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.1; 31 4.2; 34 3.5; 37 2.9; 41 2.3; 45 1.9; 49 1.6; 54 1.3; 60 0.7; 66 0.2; 72 -0.3; 79 -0.8; 87 -1.3; 96 -1.7; 106 -2.4; 116 -2.9; 128 -3.5; 141 -3.9; 155 -4.2; 170 -4.4; 187 -4.5; 206 -4.6; 227 -4.6; 249 -4.3; 274 -4.0; 302 -3.7; 332 -3.5; 365 -3.2; 402 -2.8; 442 -2.3; 486 -1.8; 535 -1.3; 588 -0.7; 647 0.1; 712 0.7; 783 1.0; 861 0.8; 947 0.4; 1042 -0.4; 1146 -1.1; 1261 -1.7; 1387 -2.2; 1526 -2.4; 1678 -2.7; 1846 -3.0; 2031 -3.3; 2234 -2.8; 2457 -1.9; 2703 -1.2; 2973 -0.8; 3270 -0.6; 3597 -0.9; 3957 -1.5; 4353 -2.6; 4788 -3.1; 5267 -2.7; 5793 -1.0; 6373 0.4; 7010 1.5; 7711 -0.7; 8482 -4.6; 9330 -8.5; 10263 -11.3; 11289 -10.6; 12418 -6.5; 13660 -2.5; 15026 -0.8; 16529 -1.8; 18182 -1.5; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 65t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 65t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.77 | 6.3 dB   |
| Peaking | 193 Hz   | 0.73 | -5.0 dB  |
| Peaking | 1475 Hz  | 3.43 | -1.3 dB  |
| Peaking | 2042 Hz  | 2.26 | -2.9 dB  |
| Peaking | 10679 Hz | 2.44 | -12.6 dB |
| Peaking | 787 Hz   | 3.48 | 2.0 dB   |
| Peaking | 4886 Hz  | 3.12 | -3.0 dB  |
| Peaking | 7063 Hz  | 3.21 | 4.1 dB   |
| Peaking | 9069 Hz  | 5.04 | -2.4 dB  |
| Peaking | 17532 Hz | 4.89 | -1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%2065t/Jabra%20Elite%2065t.png)