# Oppo PM2 2014 Stock Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.7; 25 3.5; 28 3.3; 31 3.1; 34 3.0; 37 2.9; 41 2.8; 45 2.8; 49 2.8; 54 2.8; 60 3.0; 66 2.6; 72 1.8; 79 1.4; 87 1.1; 96 0.7; 106 0.4; 116 0.2; 128 0.0; 141 -0.2; 155 -0.2; 170 -0.3; 187 -0.6; 206 -1.2; 227 -1.3; 249 -1.4; 274 -1.0; 302 -0.3; 332 0.5; 365 0.4; 402 0.3; 442 0.3; 486 -0.5; 535 -1.0; 588 -1.0; 647 -1.0; 712 -0.3; 783 0.1; 861 -0.5; 947 -0.0; 1042 -0.2; 1146 -0.4; 1261 -0.4; 1387 -1.2; 1526 -1.7; 1678 -2.2; 1846 -2.1; 2031 -1.7; 2234 -0.9; 2457 0.3; 2703 1.3; 2973 2.3; 3270 2.6; 3597 2.2; 3957 2.5; 4353 2.1; 4788 3.5; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.4; 9330 -0.6; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM2 2014 Stock Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM2 2014 Stock Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.92 | 3.8 dB  |
| Peaking | 58 Hz   | 2.04 | 2.4 dB  |
| Peaking | 1846 Hz | 1.67 | -2.8 dB |
| Peaking | 3122 Hz | 1.98 | 2.8 dB  |
| Peaking | 5693 Hz | 3    | 6.6 dB  |
| Peaking | 241 Hz  | 1.64 | -2.5 dB |
| Peaking | 402 Hz  | 0.81 | 1.9 dB  |
| Peaking | 556 Hz  | 2.08 | -2.3 dB |
| Peaking | 6582 Hz | 9.35 | 1.9 dB  |
| Peaking | 8485 Hz | 2.62 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM2%202014%20Stock%20Pads/Oppo%20PM2%202014%20Stock%20Pads.png)