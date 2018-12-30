# Shure SRH1540
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.6dB
GraphicEQ: 21 -4.2; 23 -4.8; 25 -5.3; 28 -6.0; 31 -6.5; 34 -7.0; 37 -7.4; 41 -7.8; 45 -8.0; 49 -8.2; 54 -8.3; 60 -8.4; 66 -8.3; 72 -8.1; 79 -7.8; 87 -7.4; 96 -7.1; 106 -7.1; 116 -7.1; 128 -7.1; 141 -6.6; 155 -5.5; 170 -4.3; 187 -4.6; 206 -4.1; 227 -3.7; 249 -3.7; 274 -3.6; 302 -3.9; 332 -4.1; 365 -3.8; 402 -3.5; 442 -2.8; 486 -2.4; 535 -1.9; 588 -1.1; 647 -0.7; 712 -0.3; 783 0.0; 861 0.2; 947 0.2; 1042 -0.1; 1146 0.1; 1261 0.2; 1387 -0.4; 1526 -1.1; 1678 -2.2; 1846 -3.1; 2031 -3.4; 2234 -3.1; 2457 -2.8; 2703 -2.1; 2973 -1.2; 3270 -1.4; 3597 -1.3; 3957 -1.0; 4353 -0.8; 4788 -0.5; 5267 0.5; 5793 -2.1; 6373 -3.8; 7010 -1.7; 7711 -0.5; 8482 -2.4; 9330 -3.9; 10263 -0.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1540 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-6**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 0.53 | -7.8 dB |
| Peaking | 130 Hz   | 1.04 | -3.3 dB |
| Peaking | 353 Hz   | 1.69 | -3.0 dB |
| Peaking | 2231 Hz  | 1.6  | -3.3 dB |
| Peaking | 504 Hz   | 3.54 | -0.8 dB |
| Peaking | 1429 Hz  | 0.65 | 1.2 dB  |
| Peaking | 1810 Hz  | 3.04 | -1.8 dB |
| Peaking | 7886 Hz  | 1.2  | -2.3 dB |
| Peaking | 22050 Hz | 2.17 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH1540/Shure%20SRH1540.png)