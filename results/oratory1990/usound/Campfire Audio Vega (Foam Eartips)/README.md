# Campfire Audio Vega (Foam Eartips)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -6.7; 23 -6.8; 25 -6.9; 28 -7.0; 31 -7.0; 34 -7.0; 37 -7.0; 41 -7.0; 45 -7.0; 49 -7.0; 54 -7.1; 60 -7.2; 66 -7.4; 72 -7.5; 79 -7.7; 87 -7.8; 96 -8.0; 106 -8.1; 116 -8.1; 128 -8.1; 141 -8.0; 155 -7.8; 170 -7.6; 187 -7.3; 206 -6.9; 227 -6.5; 249 -6.0; 274 -5.5; 302 -5.0; 332 -4.4; 365 -3.9; 402 -3.4; 442 -2.8; 486 -2.3; 535 -1.8; 588 -1.3; 647 -0.8; 712 -0.4; 783 -0.0; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.4; 1261 -0.8; 1387 -0.9; 1526 -0.8; 1678 -0.5; 1846 0.3; 2031 1.4; 2234 2.8; 2457 4.3; 2703 5.7; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.7; 4788 2.4; 5267 -0.1; 5793 -1.7; 6373 -3.1; 7010 -4.0; 7711 -6.8; 8482 -8.7; 9330 -7.1; 10263 -5.9; 11289 -4.3; 12418 -0.2; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Vega (Foam Eartips) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Vega (Foam Eartips) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 1.57 | -6.3 dB |
| Peaking | 29 Hz    | 0.3  | -5.8 dB |
| Peaking | 162 Hz   | 0.52 | -6.3 dB |
| Peaking | 3427 Hz  | 1.47 | 7.6 dB  |
| Peaking | 8505 Hz  | 1.7  | -9.3 dB |
| Peaking | 880 Hz   | 1.13 | 3.7 dB  |
| Peaking | 1151 Hz  | 0.65 | -3.2 dB |
| Peaking | 2499 Hz  | 3.16 | 2.3 dB  |
| Peaking | 11128 Hz | 4.32 | -3.5 dB |
| Peaking | 12114 Hz | 1.91 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Campfire%20Audio%20Vega%20(Foam%20Eartips)/Campfire%20Audio%20Vega%20(Foam%20Eartips).png)