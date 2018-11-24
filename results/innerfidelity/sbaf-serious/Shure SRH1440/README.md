# Shure SRH1440

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.7; 79 4.8; 87 4.0; 96 3.2; 106 2.6; 116 2.2; 128 1.6; 141 1.0; 155 0.5; 170 0.5; 187 0.1; 206 0.0; 227 0.0; 249 0.0; 274 0.1; 302 0.1; 332 0.2; 365 0.3; 402 0.5; 442 0.8; 486 0.9; 535 1.0; 588 1.3; 647 1.9; 712 1.5; 783 1.2; 861 0.6; 947 0.2; 1042 -0.3; 1146 -0.6; 1261 -1.2; 1387 -2.0; 1526 -3.2; 1678 -4.4; 1846 -5.3; 2031 -5.6; 2234 -6.0; 2457 -5.9; 2703 -5.7; 2973 -6.2; 3270 -6.3; 3597 -6.3; 3957 -5.8; 4353 -5.3; 4788 -3.6; 5267 -1.5; 5793 0.1; 6373 1.3; 7010 1.0; 7711 -1.6; 8482 -5.5; 9330 -7.6; 10263 -4.7; 11289 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1440 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.55 | 6.9 dB  |
| Peaking | 772 Hz   | 1.24 | 2.6 dB  |
| Peaking | 3002 Hz  | 0.61 | -7.0 dB |
| Peaking | 6455 Hz  | 2.17 | 5.3 dB  |
| Peaking | 9163 Hz  | 4.03 | -7.9 dB |
| Peaking | 42 Hz    | 2.41 | -1.1 dB |
| Peaking | 71 Hz    | 2.44 | 1.5 dB  |
| Peaking | 192 Hz   | 1.39 | -0.9 dB |
| Peaking | 1260 Hz  | 6.39 | 0.8 dB  |
| Peaking | 11775 Hz | 5.01 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH1440/Shure%20SRH1440.png)