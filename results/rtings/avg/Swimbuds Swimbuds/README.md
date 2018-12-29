# Swimbuds Swimbuds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.8; 25 0.9; 28 1.1; 31 1.2; 34 1.3; 37 1.5; 41 1.6; 45 1.8; 49 1.9; 54 1.8; 60 1.6; 66 1.3; 72 1.1; 79 0.8; 87 0.4; 96 -0.1; 106 -0.6; 116 -1.2; 128 -1.7; 141 -2.1; 155 -2.3; 170 -2.5; 187 -2.5; 206 -2.5; 227 -2.4; 249 -2.3; 274 -2.1; 302 -1.8; 332 -1.4; 365 -1.1; 402 -0.4; 442 0.2; 486 0.8; 535 1.5; 588 2.0; 647 2.2; 712 2.1; 783 1.8; 861 1.4; 947 0.6; 1042 -0.5; 1146 -1.3; 1261 -1.2; 1387 -0.3; 1526 1.2; 1678 2.7; 1846 4.0; 2031 5.1; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Swimbuds Swimbuds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Swimbuds Swimbuds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 65 Hz   | 0.59 | 3.2 dB  |
| Peaking | 171 Hz  | 0.47 | -3.8 dB |
| Peaking | 629 Hz  | 1.19 | 2.8 dB  |
| Peaking | 1223 Hz | 2.35 | -4.3 dB |
| Peaking | 3195 Hz | 0.63 | 6.9 dB  |
| Peaking | 2184 Hz | 3.62 | 1.3 dB  |
| Peaking | 3144 Hz | 1.45 | -0.8 dB |
| Peaking | 5225 Hz | 2.16 | 2.2 dB  |
| Peaking | 6353 Hz | 3.32 | 4.7 dB  |
| Peaking | 7132 Hz | 1.26 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Swimbuds%20Swimbuds/Swimbuds%20Swimbuds.png)