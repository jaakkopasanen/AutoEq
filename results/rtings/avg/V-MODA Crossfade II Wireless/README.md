# V-MODA Crossfade II Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.4; 23 -0.7; 25 -1.0; 28 -1.4; 31 -1.7; 34 -1.9; 37 -2.1; 41 -2.2; 45 -2.4; 49 -2.6; 54 -2.8; 60 -3.1; 66 -3.4; 72 -3.7; 79 -4.0; 87 -4.3; 96 -4.6; 106 -4.8; 116 -5.0; 128 -5.0; 141 -5.0; 155 -4.9; 170 -4.6; 187 -4.2; 206 -3.6; 227 -2.8; 249 -2.0; 274 -0.3; 302 0.6; 332 1.0; 365 1.8; 402 2.3; 442 2.0; 486 1.9; 535 1.9; 588 1.7; 647 1.4; 712 1.1; 783 0.7; 861 0.4; 947 0.1; 1042 -0.0; 1146 0.0; 1261 0.3; 1387 0.7; 1526 1.2; 1678 1.4; 1846 1.6; 2031 1.7; 2234 1.8; 2457 1.3; 2703 1.3; 2973 0.3; 3270 -0.3; 3597 -1.6; 3957 -0.6; 4353 2.8; 4788 5.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.4; 11289 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-MODA Crossfade II Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-MODA Crossfade II Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 122 Hz  | 0.33 | -3.1 dB |
| Peaking | 184 Hz  | 0.63 | -5.2 dB |
| Peaking | 311 Hz  | 0.53 | 4.6 dB  |
| Peaking | 369 Hz  | 1.36 | 2.0 dB  |
| Peaking | 5536 Hz | 2.78 | 7.0 dB  |
| Peaking | 1088 Hz | 1.45 | -1.8 dB |
| Peaking | 2069 Hz | 0.66 | 2.0 dB  |
| Peaking | 3703 Hz | 2.77 | -4.0 dB |
| Peaking | 4619 Hz | 7.25 | 2.9 dB  |
| Peaking | 9075 Hz | 2.2  | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/V-MODA%20Crossfade%20II%20Wireless/V-MODA%20Crossfade%20II%20Wireless.png)