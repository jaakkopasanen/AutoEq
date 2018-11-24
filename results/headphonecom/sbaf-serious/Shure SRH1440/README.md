# Shure SRH1440

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.8; 79 5.0; 87 4.4; 96 3.9; 106 3.3; 116 2.9; 128 2.4; 141 1.9; 155 1.4; 170 1.2; 187 0.9; 206 0.7; 227 0.6; 249 0.4; 274 0.4; 302 0.2; 332 0.3; 365 0.5; 402 0.6; 442 0.6; 486 0.7; 535 0.7; 588 0.7; 647 1.4; 712 1.3; 783 1.0; 861 0.6; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -1.0; 1387 -1.8; 1526 -3.1; 1678 -4.4; 1846 -5.3; 2031 -5.8; 2234 -6.2; 2457 -6.3; 2703 -6.2; 2973 -6.8; 3270 -6.5; 3597 -6.5; 3957 -6.4; 4353 -5.8; 4788 -4.0; 5267 -2.6; 5793 -0.9; 6373 -2.0; 7010 -0.2; 7711 -1.0; 8482 -3.7; 9330 -7.3; 10263 -6.2; 11289 -0.5; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 39 Hz   | 0.44 | 6.7 dB   |
| Peaking | 948 Hz  | 0.88 | 3.4 dB   |
| Peaking | 3402 Hz | 0.44 | -9.6 dB  |
| Peaking | 7460 Hz | 0.68 | 7.2 dB   |
| Peaking | 9544 Hz | 3.15 | -10.5 dB |
| Peaking | 43 Hz   | 2.25 | -0.7 dB  |
| Peaking | 71 Hz   | 3.56 | 0.9 dB   |
| Peaking | 2644 Hz | 5.49 | 1.7 dB   |
| Peaking | 2904 Hz | 2    | -1.4 dB  |
| Peaking | 3220 Hz | 5.27 | 1.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH1440/Shure%20SRH1440.png)