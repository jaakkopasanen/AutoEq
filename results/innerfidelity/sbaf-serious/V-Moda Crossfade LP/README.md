# V-Moda Crossfade LP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.7; 25 2.0; 28 1.0; 31 0.2; 34 -0.6; 37 -1.3; 41 -2.0; 45 -2.5; 49 -2.8; 54 -3.1; 60 -3.2; 66 -3.3; 72 -3.8; 79 -4.1; 87 -3.9; 96 -4.4; 106 -4.7; 116 -5.0; 128 -5.2; 141 -5.4; 155 -5.4; 170 -5.2; 187 -5.2; 206 -4.8; 227 -3.9; 249 -2.8; 274 -1.8; 302 -0.1; 332 1.5; 365 2.6; 402 3.3; 442 4.2; 486 4.2; 535 3.9; 588 3.3; 647 2.1; 712 0.9; 783 0.5; 861 0.2; 947 -0.0; 1042 0.0; 1146 -0.3; 1261 -0.9; 1387 -1.7; 1526 -2.1; 1678 -2.4; 1846 -2.4; 2031 -2.7; 2234 -3.5; 2457 -2.8; 2703 -2.3; 2973 -1.5; 3270 -1.6; 3597 -0.5; 3957 2.0; 4353 3.5; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.1; 10263 -0.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade LP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade LP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.23 | 5.5 dB  |
| Peaking | 225 Hz   | 0.7  | -7.2 dB |
| Peaking | 407 Hz   | 0.56 | 13.3 dB |
| Peaking | 579 Hz   | 0.07 | -5.6 dB |
| Peaking | 5296 Hz  | 1.53 | 10.4 dB |
| Peaking | 740 Hz   | 5.26 | -1.0 dB |
| Peaking | 1151 Hz  | 4.53 | 0.9 dB  |
| Peaking | 6533 Hz  | 6.1  | 2.8 dB  |
| Peaking | 7183 Hz  | 2.39 | -1.6 dB |
| Peaking | 13130 Hz | 1.14 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20LP/V-Moda%20Crossfade%20LP.png)