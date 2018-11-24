# Venture Electronics Duke

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.8dB
GraphicEQ: 21 0.0; 23 0.2; 25 -0.0; 28 -0.2; 31 -0.4; 34 -0.6; 37 -0.8; 41 -1.0; 45 -1.2; 49 -1.4; 54 -1.7; 60 -2.1; 66 -2.5; 72 -2.8; 79 -3.2; 87 -3.5; 96 -4.0; 106 -4.3; 116 -4.5; 128 -4.8; 141 -5.0; 155 -5.1; 170 -5.2; 187 -5.2; 206 -5.2; 227 -5.0; 249 -4.9; 274 -4.6; 302 -4.4; 332 -4.0; 365 -3.6; 402 -3.2; 442 -2.7; 486 -2.3; 535 -1.8; 588 -1.1; 647 -0.7; 712 -0.4; 783 0.1; 861 0.1; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.5; 1387 -1.0; 1526 -1.4; 1678 -1.6; 1846 -1.6; 2031 -0.3; 2234 -0.5; 2457 -0.8; 2703 -2.8; 2973 -2.9; 3270 -0.4; 3597 1.4; 3957 1.6; 4353 0.4; 4788 0.4; 5267 0.7; 5793 0.1; 6373 -4.4; 7010 -8.5; 7711 -8.3; 8482 -4.9; 9330 -0.5; 10263 0.0; 11289 -0.3; 12418 -2.5; 13660 -0.5; 15026 0.0; 16529 0.0; 18182 -1.0; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Venture Electronics Duke GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venture Electronics Duke ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 122 Hz  | 0.69 | -4.0 dB  |
| Peaking | 228 Hz  | 1.27 | -2.6 dB  |
| Peaking | 372 Hz  | 1.86 | -1.9 dB  |
| Peaking | 1747 Hz | 2.37 | -1.5 dB  |
| Peaking | 7410 Hz | 4.2  | -10.1 dB |
| Peaking | 2884 Hz | 4.56 | -4.4 dB  |
| Peaking | 3631 Hz | 5.38 | 1.3 dB   |
| Peaking | 5104 Hz | 0.68 | 2.4 dB   |
| Peaking | 9253 Hz | 1.03 | -4.1 dB  |
| Peaking | 9867 Hz | 3.06 | 4.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Venture%20Electronics%20Duke/Venture%20Electronics%20Duke.png)