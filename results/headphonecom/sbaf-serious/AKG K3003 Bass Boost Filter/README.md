# AKG K3003 Bass Boost Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 -1.7; 23 -2.3; 25 -2.7; 28 -3.3; 31 -3.8; 34 -4.2; 37 -4.6; 41 -5.1; 45 -5.5; 49 -5.8; 54 -6.3; 60 -6.8; 66 -7.1; 72 -7.5; 79 -8.0; 87 -8.3; 96 -8.6; 106 -8.8; 116 -8.9; 128 -9.1; 141 -9.2; 155 -9.3; 170 -9.3; 187 -9.2; 206 -8.9; 227 -8.6; 249 -8.3; 274 -7.8; 302 -7.3; 332 -6.7; 365 -5.9; 402 -5.2; 442 -4.6; 486 -3.9; 535 -3.2; 588 -2.4; 647 -1.6; 712 -1.0; 783 -0.5; 861 -0.1; 947 -0.1; 1042 -0.2; 1146 -0.5; 1261 -0.6; 1387 -0.5; 1526 -0.0; 1678 -1.0; 1846 -1.7; 2031 -2.1; 2234 -2.2; 2457 -1.7; 2703 -0.3; 2973 2.2; 3270 4.6; 3597 5.7; 3957 4.1; 4353 0.6; 4788 -2.6; 5267 -4.2; 5793 -0.2; 6373 3.1; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -3.0; 10263 -1.7; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 Bass Boost Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Bass Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 95 Hz    | 0.42 | -7.6 dB |
| Peaking | 248 Hz   | 0.85 | -4.5 dB |
| Peaking | 3678 Hz  | 2.53 | 12.6 dB |
| Peaking | 4832 Hz  | 0.88 | -8.5 dB |
| Peaking | 6576 Hz  | 3.2  | 8.7 dB  |
| Peaking | 909 Hz   | 2.25 | 1.3 dB  |
| Peaking | 2263 Hz  | 3.18 | -1.7 dB |
| Peaking | 3071 Hz  | 7.28 | 1.6 dB  |
| Peaking | 9634 Hz  | 6.84 | -4.1 dB |
| Peaking | 10637 Hz | 1.74 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K3003%20Bass%20Boost%20Filter/AKG%20K3003%20Bass%20Boost%20Filter.png)