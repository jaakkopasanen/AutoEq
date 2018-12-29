# AKG K3003 Bass Boost Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 -0.7; 23 -1.2; 25 -1.6; 28 -2.2; 31 -2.7; 34 -3.1; 37 -3.5; 41 -4.0; 45 -4.4; 49 -4.7; 54 -5.1; 60 -5.6; 66 -6.0; 72 -6.5; 79 -6.8; 87 -7.4; 96 -7.8; 106 -8.1; 116 -8.2; 128 -8.5; 141 -8.6; 155 -8.7; 170 -8.6; 187 -8.5; 206 -8.4; 227 -8.1; 249 -7.8; 274 -7.3; 302 -6.9; 332 -6.3; 365 -5.7; 402 -5.0; 442 -4.2; 486 -3.8; 535 -3.0; 588 -2.1; 647 -1.4; 712 -0.9; 783 -0.3; 861 -0.1; 947 -0.1; 1042 -0.0; 1146 -0.1; 1261 -0.2; 1387 -0.2; 1526 -0.4; 1678 -1.2; 1846 -1.8; 2031 -2.0; 2234 -2.3; 2457 -1.7; 2703 -0.2; 2973 2.4; 3270 4.6; 3597 5.1; 3957 3.6; 4353 0.0; 4788 -3.0; 5267 -4.6; 5793 -1.8; 6373 1.7; 7010 2.4; 7711 0.3; 8482 0.0; 9330 -2.1; 10263 -1.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 Bass Boost Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Bass Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 109 Hz  | 0.46 | -7.3 dB |
| Peaking | 268 Hz  | 0.9  | -3.8 dB |
| Peaking | 2427 Hz | 1.7  | -7.6 dB |
| Peaking | 3325 Hz | 1.09 | 8.9 dB  |
| Peaking | 5007 Hz | 3.47 | -8.5 dB |
| Peaking | 482 Hz  | 2.29 | -0.8 dB |
| Peaking | 806 Hz  | 1.4  | 1.0 dB  |
| Peaking | 1764 Hz | 6.22 | -0.9 dB |
| Peaking | 6745 Hz | 8.98 | 2.9 dB  |
| Peaking | 9614 Hz | 5.57 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K3003%20Bass%20Boost%20Filter/AKG%20K3003%20Bass%20Boost%20Filter.png)