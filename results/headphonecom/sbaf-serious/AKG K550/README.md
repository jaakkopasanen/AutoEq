# AKG K 550
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.3; 28 0.9; 31 0.6; 34 0.4; 37 0.2; 41 0.0; 45 -0.1; 49 -0.1; 54 -0.1; 60 -0.2; 66 -0.3; 72 -0.1; 79 0.5; 87 1.7; 96 2.0; 106 0.6; 116 -0.6; 128 -1.5; 141 -1.7; 155 -1.4; 170 0.1; 187 -1.6; 206 -1.8; 227 -1.8; 249 -1.9; 274 -1.6; 302 -1.5; 332 -1.3; 365 -0.9; 402 -0.6; 442 -0.4; 486 -0.1; 535 0.2; 588 0.7; 647 1.2; 712 1.4; 783 1.5; 861 0.5; 947 0.3; 1042 -0.1; 1146 -0.5; 1261 -0.8; 1387 -1.2; 1526 -2.0; 1678 -1.6; 1846 -0.7; 2031 -0.0; 2234 0.6; 2457 1.0; 2703 1.3; 2973 2.4; 3270 3.9; 3597 5.5; 3957 5.9; 4353 4.3; 4788 3.3; 5267 -0.1; 5793 -0.6; 6373 3.7; 7010 2.5; 7711 0.2; 8482 -5.1; 9330 -6.6; 10263 -1.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K 550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K 550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 1.27 | 3.5 dB  |
| Peaking | 236 Hz   | 1.54 | -2.1 dB |
| Peaking | 3812 Hz  | 2.9  | 6.4 dB  |
| Peaking | 6685 Hz  | 8.42 | 4.8 dB  |
| Peaking | 9028 Hz  | 5.32 | -8.0 dB |
| Peaking | 95 Hz    | 5.07 | 2.6 dB  |
| Peaking | 134 Hz   | 4.81 | -1.6 dB |
| Peaking | 717 Hz   | 3    | 1.7 dB  |
| Peaking | 1540 Hz  | 3.26 | -2.2 dB |
| Peaking | 11090 Hz | 4.45 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K550/AKG%20K%20550.png)