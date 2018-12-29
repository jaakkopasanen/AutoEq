# Oppo PM2 2014 PM1 Alt Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.6; 25 3.5; 28 3.4; 31 3.3; 34 3.2; 37 3.2; 41 3.2; 45 3.4; 49 3.5; 54 3.2; 60 3.3; 66 3.0; 72 2.4; 79 1.8; 87 1.5; 96 1.0; 106 0.7; 116 0.6; 128 0.3; 141 0.2; 155 0.1; 170 0.1; 187 -0.3; 206 -0.8; 227 -1.0; 249 -1.1; 274 -0.5; 302 -0.1; 332 0.7; 365 0.5; 402 0.3; 442 0.3; 486 -0.2; 535 -0.7; 588 -0.6; 647 -0.7; 712 -0.1; 783 0.3; 861 -0.3; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 0.0; 1387 -0.5; 1526 -0.7; 1678 -0.7; 1846 -0.3; 2031 0.1; 2234 0.8; 2457 1.8; 2703 2.7; 2973 3.8; 3270 4.2; 3597 4.2; 3957 4.9; 4353 4.8; 4788 5.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.4; 9330 -1.9; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM2 2014 PM1 Alt Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM2 2014 PM1 Alt Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.67 | 3.4 dB  |
| Peaking | 57 Hz   | 1.44 | 2.4 dB  |
| Peaking | 228 Hz  | 3.33 | -1.4 dB |
| Peaking | 5283 Hz | 1.01 | 6.9 dB  |
| Peaking | 8706 Hz | 2.39 | -4.6 dB |
| Peaking | 346 Hz  | 5.14 | 0.9 dB  |
| Peaking | 576 Hz  | 4.05 | -0.8 dB |
| Peaking | 1735 Hz | 1.93 | -1.6 dB |
| Peaking | 3038 Hz | 2.57 | 1.5 dB  |
| Peaking | 4458 Hz | 5.78 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM2%202014%20PM1%20Alt%20Pads/Oppo%20PM2%202014%20PM1%20Alt%20Pads.png)