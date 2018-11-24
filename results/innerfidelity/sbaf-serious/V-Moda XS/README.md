# V-Moda XS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 -2.2; 23 -2.6; 25 -3.0; 28 -3.4; 31 -3.8; 34 -4.0; 37 -4.2; 41 -4.4; 45 -4.6; 49 -4.7; 54 -4.8; 60 -4.8; 66 -4.9; 72 -5.0; 79 -5.0; 87 -5.2; 96 -5.2; 106 -5.0; 116 -5.0; 128 -5.1; 141 -5.1; 155 -4.9; 170 -4.5; 187 -4.3; 206 -3.6; 227 -3.3; 249 -3.8; 274 -2.8; 302 -1.6; 332 -0.4; 365 0.7; 402 1.0; 442 1.5; 486 1.7; 535 2.1; 588 2.6; 647 2.6; 712 2.2; 783 2.1; 861 1.2; 947 0.5; 1042 -0.3; 1146 -0.9; 1261 -1.1; 1387 -1.2; 1526 -1.0; 1678 -0.8; 1846 -0.4; 2031 -0.7; 2234 -0.4; 2457 -0.6; 2703 -1.6; 2973 -2.4; 3270 -2.0; 3597 0.1; 3957 3.1; 4353 3.5; 4788 0.8; 5267 3.6; 5793 2.3; 6373 2.7; 7010 2.1; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda XS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda XS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 190 Hz  | 0.13 | -6.0 dB |
| Peaking | 550 Hz  | 0.74 | 8.0 dB  |
| Peaking | 3116 Hz | 3.93 | -2.5 dB |
| Peaking | 4094 Hz | 5.54 | 4.2 dB  |
| Peaking | 5854 Hz | 2.64 | 3.1 dB  |
| Peaking | 254 Hz  | 7.21 | -1.0 dB |
| Peaking | 358 Hz  | 4.78 | 0.9 dB  |
| Peaking | 513 Hz  | 2.84 | -1.0 dB |
| Peaking | 1056 Hz | 0.84 | 1.5 dB  |
| Peaking | 1187 Hz | 1.77 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20XS/V-Moda%20XS.png)