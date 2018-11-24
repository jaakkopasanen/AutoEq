# Shure SRH440

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.8; 41 4.8; 45 3.7; 49 2.8; 54 1.8; 60 0.7; 66 -0.2; 72 -0.7; 79 -0.9; 87 -0.5; 96 0.3; 106 -1.0; 116 -2.5; 128 -2.9; 141 -2.3; 155 -1.8; 170 -0.6; 187 -1.5; 206 -1.2; 227 -0.9; 249 -0.9; 274 -0.8; 302 -0.8; 332 -0.8; 365 -1.9; 402 -1.9; 442 -1.4; 486 -1.3; 535 -1.1; 588 -0.7; 647 -0.5; 712 -0.5; 783 -0.3; 861 -0.3; 947 -0.2; 1042 0.4; 1146 0.7; 1261 0.3; 1387 -0.4; 1526 -1.1; 1678 -1.5; 1846 -1.3; 2031 -1.0; 2234 -0.3; 2457 0.5; 2703 0.2; 2973 0.5; 3270 -0.9; 3597 -0.9; 3957 0.4; 4353 0.7; 4788 2.1; 5267 3.1; 5793 4.2; 6373 5.5; 7010 2.5; 7711 -0.5; 8482 -4.2; 9330 -6.0; 10263 -5.1; 11289 -0.8; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 1.05 | 6.9 dB  |
| Peaking | 128 Hz   | 1.59 | -2.7 dB |
| Peaking | 416 Hz   | 1.63 | -1.6 dB |
| Peaking | 6231 Hz  | 3.03 | 6.6 dB  |
| Peaking | 9296 Hz  | 2.99 | -7.3 dB |
| Peaking | 70 Hz    | 2.71 | -3.2 dB |
| Peaking | 70 Hz    | 1.32 | 1.7 dB  |
| Peaking | 1751 Hz  | 4.19 | -1.7 dB |
| Peaking | 10530 Hz | 6.29 | -2.4 dB |
| Peaking | 11372 Hz | 3.02 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH440/Shure%20SRH440.png)