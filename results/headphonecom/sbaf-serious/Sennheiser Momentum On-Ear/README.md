# Sennheiser Momentum On-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.4; 23 -2.6; 25 -2.8; 28 -3.0; 31 -3.1; 34 -3.2; 37 -3.3; 41 -3.4; 45 -3.5; 49 -3.5; 54 -3.6; 60 -3.8; 66 -3.9; 72 -3.8; 79 -3.6; 87 -3.6; 96 -4.1; 106 -4.3; 116 -4.3; 128 -4.3; 141 -4.1; 155 -3.8; 170 -3.5; 187 -3.1; 206 -2.5; 227 -1.7; 249 -0.8; 274 0.4; 302 0.8; 332 1.4; 365 1.9; 402 2.1; 442 2.0; 486 1.8; 535 1.5; 588 1.2; 647 0.7; 712 0.5; 783 0.4; 861 0.3; 947 0.3; 1042 -0.2; 1146 -1.0; 1261 -2.1; 1387 -3.3; 1526 -4.5; 1678 -5.5; 1846 -5.5; 2031 -4.8; 2234 -3.7; 2457 -1.9; 2703 0.2; 2973 1.7; 3270 3.0; 3597 4.7; 3957 6.0; 4353 6.0; 4788 0.9; 5267 1.3; 5793 2.7; 6373 0.8; 7010 -3.1; 7711 -3.4; 8482 -2.7; 9330 -2.5; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum On-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 47 Hz   |  0.62 | -3.7 dB |
| Peaking | 132 Hz  |  1.64 | -3.6 dB |
| Peaking | 1829 Hz |  2.12 | -6.6 dB |
| Peaking | 3936 Hz |  2.13 | 6.7 dB  |
| Peaking | 7835 Hz |  3.1  | -4.3 dB |
| Peaking | 201 Hz  |  2.69 | -1.7 dB |
| Peaking | 401 Hz  |  1.18 | 2.6 dB  |
| Peaking | 977 Hz  |  3.47 | 0.6 dB  |
| Peaking | 1395 Hz |  3.97 | -1.1 dB |
| Peaking | 5943 Hz | 11.25 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Momentum%20On-Ear/Sennheiser%20Momentum%20On-Ear.png)