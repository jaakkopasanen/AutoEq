# Sennheiser IE 800 sample A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.8; 23 -4.9; 25 -5.0; 28 -5.1; 31 -5.2; 34 -5.2; 37 -5.3; 41 -5.3; 45 -5.3; 49 -5.3; 54 -5.3; 60 -5.3; 66 -5.3; 72 -5.4; 79 -5.4; 87 -5.5; 96 -5.5; 106 -5.4; 116 -5.2; 128 -5.1; 141 -4.9; 155 -4.7; 170 -4.4; 187 -4.1; 206 -3.7; 227 -3.3; 249 -3.0; 274 -2.6; 302 -2.2; 332 -1.8; 365 -1.4; 402 -1.1; 442 -0.6; 486 -0.5; 535 -0.1; 588 0.4; 647 0.5; 712 0.6; 783 0.8; 861 0.6; 947 0.3; 1042 -0.0; 1146 -0.2; 1261 -0.4; 1387 -0.7; 1526 -0.9; 1678 -0.7; 1846 0.2; 2031 1.3; 2234 2.9; 2457 4.8; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.8; 4788 2.1; 5267 1.2; 5793 2.4; 6373 5.4; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -2.3; 10263 -3.0; 11289 -0.3; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.27 | -5.0 dB |
| Peaking | 150 Hz  | 0.74 | -2.7 dB |
| Peaking | 3286 Hz | 1.64 | 7.0 dB  |
| Peaking | 6439 Hz | 7.04 | 5.0 dB  |
| Peaking | 9920 Hz | 4.28 | -3.7 dB |
| Peaking | 724 Hz  | 2.01 | 1.2 dB  |
| Peaking | 1587 Hz | 2.02 | -1.9 dB |
| Peaking | 2556 Hz | 3.92 | 2.6 dB  |
| Peaking | 3838 Hz | 1.65 | -2.1 dB |
| Peaking | 4086 Hz | 5.14 | 3.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800%20sample%20A/Sennheiser%20IE%20800%20sample%20A.png)