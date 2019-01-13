# Sony MDR-7509HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.9; 66 4.8; 72 3.6; 79 2.3; 87 1.1; 96 0.6; 106 0.7; 116 0.4; 128 -0.3; 141 -1.4; 155 -2.3; 170 -1.5; 187 -2.2; 206 -1.7; 227 -1.6; 249 -1.2; 274 -0.6; 302 -0.2; 332 -0.4; 365 -1.5; 402 -2.7; 442 -3.4; 486 -3.6; 535 -3.1; 588 -1.6; 647 0.1; 712 -1.3; 783 -0.5; 861 -0.1; 947 0.1; 1042 0.0; 1146 -0.4; 1261 -0.9; 1387 -2.2; 1526 -4.3; 1678 -5.8; 1846 -6.1; 2031 -7.2; 2234 -6.6; 2457 -4.3; 2703 -1.3; 2973 0.5; 3270 2.1; 3597 4.2; 3957 6.0; 4353 6.0; 4788 6.0; 5267 4.2; 5793 4.1; 6373 5.5; 7010 2.5; 7711 -0.0; 8482 -4.3; 9330 -5.0; 10263 -0.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7509HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7509HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.91 | 7.2 dB  |
| Peaking | 2048 Hz | 1.71 | -8.6 dB |
| Peaking | 4149 Hz | 1.52 | 7.4 dB  |
| Peaking | 6403 Hz | 5.61 | 4.2 dB  |
| Peaking | 8929 Hz | 4.29 | -6.7 dB |
| Peaking | 39 Hz   | 3.51 | -1.3 dB |
| Peaking | 60 Hz   | 3.09 | 2.7 dB  |
| Peaking | 170 Hz  | 1.58 | -2.5 dB |
| Peaking | 473 Hz  | 3.07 | -3.8 dB |
| Peaking | 1050 Hz | 2.85 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7509HD/Sony%20MDR-7509HD.png)