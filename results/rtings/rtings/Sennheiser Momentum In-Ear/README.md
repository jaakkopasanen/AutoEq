# Sennheiser Momentum In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 21 -1.9; 23 -1.9; 25 -2.0; 28 -2.1; 31 -2.2; 34 -2.3; 37 -2.4; 41 -2.5; 45 -2.7; 49 -2.8; 54 -3.0; 60 -3.5; 66 -4.0; 72 -4.4; 79 -4.8; 87 -5.4; 96 -5.9; 106 -6.5; 116 -7.1; 128 -7.6; 141 -8.0; 155 -8.2; 170 -8.3; 187 -8.2; 206 -8.0; 227 -7.9; 249 -7.7; 274 -7.3; 302 -6.8; 332 -6.2; 365 -5.5; 402 -4.9; 442 -4.2; 486 -3.4; 535 -2.5; 588 -1.6; 647 -0.6; 712 0.3; 783 0.7; 861 0.8; 947 0.4; 1042 -0.3; 1146 -0.8; 1261 -0.9; 1387 -0.9; 1526 -0.8; 1678 -0.8; 1846 -0.7; 2031 -0.4; 2234 0.8; 2457 2.5; 2703 3.6; 2973 4.0; 3270 3.8; 3597 3.4; 3957 2.9; 4353 2.1; 4788 2.4; 5267 2.7; 5793 1.0; 6373 -4.2; 7010 -6.4; 7711 -3.7; 8482 -4.0; 9330 -9.2; 10263 -11.2; 11289 -7.3; 12418 -4.9; 13660 -4.1; 15026 -0.2; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 97 Hz    | 0.4  | -3.2 dB  |
| Peaking | 210 Hz   | 0.69 | -6.3 dB  |
| Peaking | 3901 Hz  | 1    | 4.2 dB   |
| Peaking | 6779 Hz  | 6.36 | -6.6 dB  |
| Peaking | 10221 Hz | 2.25 | -11.8 dB |
| Peaking | 22 Hz    | 1.92 | -0.9 dB  |
| Peaking | 796 Hz   | 2.93 | 2.4 dB   |
| Peaking | 2026 Hz  | 1.23 | -3.2 dB  |
| Peaking | 2594 Hz  | 1.49 | 3.2 dB   |
| Peaking | 4050 Hz  | 5.68 | -1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)