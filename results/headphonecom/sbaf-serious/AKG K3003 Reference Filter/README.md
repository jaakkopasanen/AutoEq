# AKG K3003 Reference Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.4; 25 2.0; 28 1.4; 31 0.9; 34 0.5; 37 0.2; 41 -0.3; 45 -0.7; 49 -1.0; 54 -1.4; 60 -1.9; 66 -2.4; 72 -2.7; 79 -3.2; 87 -3.5; 96 -3.8; 106 -4.1; 116 -4.3; 128 -4.6; 141 -4.6; 155 -4.9; 170 -4.8; 187 -4.8; 206 -4.7; 227 -4.6; 249 -4.3; 274 -4.0; 302 -3.7; 332 -3.2; 365 -2.7; 402 -2.2; 442 -1.8; 486 -1.5; 535 -1.1; 588 -0.6; 647 -0.2; 712 0.2; 783 0.4; 861 0.3; 947 0.2; 1042 -0.3; 1146 -0.6; 1261 -0.9; 1387 -1.0; 1526 -1.6; 1678 -2.2; 1846 -2.4; 2031 -2.2; 2234 -1.8; 2457 -0.7; 2703 1.1; 2973 2.9; 3270 5.2; 3597 6.0; 3957 6.0; 4353 1.6; 4788 -3.0; 5267 -2.1; 5793 2.0; 6373 4.9; 7010 2.5; 7711 0.3; 8482 -4.2; 9330 -8.7; 10263 -6.3; 11289 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 Reference Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 1.15 | 3.3 dB   |
| Peaking | 158 Hz  | 0.52 | -5.0 dB  |
| Peaking | 3589 Hz | 4.61 | 7.3 dB   |
| Peaking | 6541 Hz | 6.61 | 5.9 dB   |
| Peaking | 9508 Hz | 4.59 | -10.0 dB |
| Peaking | 811 Hz  | 1.74 | 1.6 dB   |
| Peaking | 2188 Hz | 0.99 | -3.1 dB  |
| Peaking | 2847 Hz | 4.04 | 2.7 dB   |
| Peaking | 4573 Hz | 1.75 | 4.3 dB   |
| Peaking | 4870 Hz | 4.82 | -8.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K3003%20Reference%20Filter/AKG%20K3003%20Reference%20Filter.png)