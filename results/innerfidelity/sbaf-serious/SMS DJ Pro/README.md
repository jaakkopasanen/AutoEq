# SMS DJ Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.3; 23 -4.5; 25 -4.7; 28 -4.8; 31 -4.8; 34 -4.7; 37 -4.6; 41 -4.4; 45 -4.1; 49 -3.8; 54 -3.4; 60 -2.9; 66 -2.2; 72 -1.9; 79 -2.1; 87 -3.5; 96 -5.3; 106 -5.0; 116 -3.6; 128 -2.5; 141 -2.1; 155 -1.0; 170 -0.8; 187 -1.1; 206 -1.3; 227 -1.3; 249 -1.7; 274 -2.0; 302 -2.2; 332 -2.3; 365 -3.6; 402 -4.4; 442 -3.6; 486 -3.5; 535 -2.9; 588 -2.1; 647 -1.5; 712 -0.5; 783 0.5; 861 -0.4; 947 -0.0; 1042 0.1; 1146 0.4; 1261 0.3; 1387 -0.2; 1526 -0.9; 1678 -1.2; 1846 -0.8; 2031 0.4; 2234 1.4; 2457 2.6; 2703 3.7; 2973 4.6; 3270 4.6; 3597 4.4; 3957 3.2; 4353 3.7; 4788 2.0; 5267 4.2; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SMS DJ Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SMS DJ Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 30 Hz   |  0.69 | -5.0 dB |
| Peaking | 103 Hz  |  3.14 | -4.5 dB |
| Peaking | 416 Hz  |  1.55 | -4.1 dB |
| Peaking | 3227 Hz |  2.17 | 4.9 dB  |
| Peaking | 5936 Hz |  3.74 | 6.1 dB  |
| Peaking | 768 Hz  | 11.95 | 1.5 dB  |
| Peaking | 1169 Hz |  3.71 | 0.8 dB  |
| Peaking | 1701 Hz |  3.04 | -1.8 dB |
| Peaking | 2524 Hz |  4.5  | 0.9 dB  |
| Peaking | 8228 Hz |  4.81 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SMS%20DJ%20Pro/SMS%20DJ%20Pro.png)