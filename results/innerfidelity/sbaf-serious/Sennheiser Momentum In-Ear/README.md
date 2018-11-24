# Sennheiser Momentum In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -6.8; 23 -6.9; 25 -6.9; 28 -7.0; 31 -7.1; 34 -7.2; 37 -7.2; 41 -7.3; 45 -7.4; 49 -7.4; 54 -7.5; 60 -7.7; 66 -7.8; 72 -8.0; 79 -8.1; 87 -8.3; 96 -8.5; 106 -8.4; 116 -8.3; 128 -8.3; 141 -8.1; 155 -8.0; 170 -7.7; 187 -7.3; 206 -7.0; 227 -6.4; 249 -6.0; 274 -5.5; 302 -4.9; 332 -4.3; 365 -3.7; 402 -3.2; 442 -2.4; 486 -2.0; 535 -1.5; 588 -0.7; 647 -0.2; 712 0.0; 783 0.4; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.7; 1387 -1.2; 1526 -1.7; 1678 -1.9; 1846 -1.6; 2031 -1.0; 2234 -0.3; 2457 1.1; 2703 2.4; 2973 4.4; 3270 5.8; 3597 6.0; 3957 5.3; 4353 2.7; 4788 1.3; 5267 0.7; 5793 -1.6; 6373 -5.3; 7010 -4.0; 7711 -1.5; 8482 -0.0; 9330 0.0; 10263 -0.5; 11289 -2.6; 12418 -3.4; 13660 -3.2; 15026 -0.1; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.88 | -6.6 dB |
| Peaking | 62 Hz    | 0.37 | -6.5 dB |
| Peaking | 186 Hz   | 0.69 | -4.2 dB |
| Peaking | 3554 Hz  | 2.71 | 7.0 dB  |
| Peaking | 6579 Hz  | 4.22 | -6.1 dB |
| Peaking | 10 Hz    | 1.35 | 1.5 dB  |
| Peaking | 789 Hz   | 2.36 | 1.3 dB  |
| Peaking | 1725 Hz  | 2.15 | -2.5 dB |
| Peaking | 8253 Hz  | 0.19 | 0.5 dB  |
| Peaking | 12673 Hz | 2.51 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)