# Sennheiser HD 598 Cs

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.1; 25 3.9; 28 3.7; 31 3.6; 34 3.6; 37 3.6; 41 3.6; 45 3.5; 49 3.4; 54 3.2; 60 2.9; 66 2.6; 72 2.3; 79 2.1; 87 1.6; 96 1.1; 106 0.7; 116 0.2; 128 0.0; 141 0.1; 155 0.2; 170 0.5; 187 0.9; 206 1.7; 227 2.5; 249 3.3; 274 3.7; 302 3.8; 332 3.2; 365 2.5; 402 1.5; 442 0.5; 486 -0.4; 535 -0.4; 588 -0.3; 647 -0.2; 712 -0.3; 783 -0.3; 861 -0.2; 947 -0.0; 1042 0.1; 1146 0.2; 1261 0.3; 1387 0.2; 1526 0.1; 1678 0.0; 1846 -0.1; 2031 -0.2; 2234 0.6; 2457 2.0; 2703 2.9; 2973 2.4; 3270 0.7; 3597 -0.4; 3957 1.6; 4353 2.6; 4788 4.5; 5267 6.0; 5793 6.0; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.0; 18182 -4.2; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 Cs GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 Cs ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.83 | 4.0 dB  |
| Peaking | 53 Hz    | 1.38 | 2.5 dB  |
| Peaking | 286 Hz   | 2.36 | 4.1 dB  |
| Peaking | 2725 Hz  | 5.41 | 2.8 dB  |
| Peaking | 5560 Hz  | 2.77 | 6.8 dB  |
| Peaking | 138 Hz   | 1.92 | -1.2 dB |
| Peaking | 208 Hz   | 0.32 | 0.6 dB  |
| Peaking | 555 Hz   | 1.7  | -1.2 dB |
| Peaking | 1950 Hz  | 4.78 | -0.5 dB |
| Peaking | 19767 Hz | 1.73 | -8.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20598%20Cs/Sennheiser%20HD%20598%20Cs.png)