# Audeze LCD-3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.5; 25 1.4; 28 0.9; 31 0.5; 34 0.7; 37 0.7; 41 0.1; 45 -0.3; 49 -0.9; 54 -0.9; 60 -0.8; 66 -0.9; 72 -1.1; 79 -1.3; 87 -1.6; 96 -1.8; 106 -2.0; 116 -2.2; 128 -2.4; 141 -2.6; 155 -2.8; 170 -3.1; 187 -3.3; 206 -3.5; 227 -3.5; 249 -3.7; 274 -3.5; 302 -2.8; 332 -2.2; 365 -2.0; 402 -2.4; 442 -3.0; 486 -3.0; 535 -2.6; 588 -2.4; 647 -2.4; 712 -2.1; 783 -2.3; 861 -2.2; 947 -0.7; 1042 0.5; 1146 1.1; 1261 -0.3; 1387 -0.4; 1526 -0.8; 1678 -0.1; 1846 1.3; 2031 2.6; 2234 0.8; 2457 1.7; 2703 1.6; 2973 1.3; 3270 2.3; 3597 5.1; 3957 6.0; 4353 6.0; 4788 4.1; 5267 1.5; 5793 1.1; 6373 2.4; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.6; 16529 -6.1; 18182 -8.1; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 201 Hz   | 0.66 | -3.3 dB |
| Peaking | 605 Hz   | 1.47 | -2.0 dB |
| Peaking | 2050 Hz  | 6.02 | 2.1 dB  |
| Peaking | 4113 Hz  | 2.27 | 6.4 dB  |
| Peaking | 18283 Hz | 1.6  | -9.1 dB |
| Peaking | 24 Hz    | 1.86 | 1.6 dB  |
| Peaking | 1097 Hz  | 4.22 | 3.5 dB  |
| Peaking | 1098 Hz  | 1.79 | -1.8 dB |
| Peaking | 13640 Hz | 3.01 | 1.6 dB  |
| Peaking | 21128 Hz | 1.37 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-3/Audeze%20LCD-3.png)