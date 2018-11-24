# Jabra Elite 25e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 -7.5; 23 -7.7; 25 -7.9; 28 -8.0; 31 -8.1; 34 -8.1; 37 -8.1; 41 -8.1; 45 -8.0; 49 -8.0; 54 -8.0; 60 -8.2; 66 -8.3; 72 -8.4; 79 -8.5; 87 -8.8; 96 -9.0; 106 -9.3; 116 -9.6; 128 -9.8; 141 -9.9; 155 -9.9; 170 -9.8; 187 -9.6; 206 -9.5; 227 -9.2; 249 -8.7; 274 -8.0; 302 -7.3; 332 -6.6; 365 -5.9; 402 -5.2; 442 -4.4; 486 -3.5; 535 -2.6; 588 -1.7; 647 -0.8; 712 0.1; 783 0.5; 861 0.4; 947 0.4; 1042 -0.3; 1146 -1.1; 1261 -1.5; 1387 -1.7; 1526 -1.7; 1678 -1.8; 1846 -2.0; 2031 -2.0; 2234 -1.5; 2457 -1.1; 2703 -0.8; 2973 -0.6; 3270 0.4; 3597 1.3; 3957 1.1; 4353 0.2; 4788 0.5; 5267 1.5; 5793 3.0; 6373 1.3; 7010 0.5; 7711 -1.4; 8482 -2.4; 9330 -0.4; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.9; 16529 -5.8; 18182 -6.8; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 25e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 25e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.19 | -7.7 dB |
| Peaking | 207 Hz   | 0.75 | -6.2 dB |
| Peaking | 1865 Hz  | 2.54 | -2.0 dB |
| Peaking | 5825 Hz  | 4.63 | 3.1 dB  |
| Peaking | 18663 Hz | 1.13 | -7.8 dB |
| Peaking | 398 Hz   | 2.42 | -0.9 dB |
| Peaking | 771 Hz   | 2.82 | 2.2 dB  |
| Peaking | 3687 Hz  | 6.65 | 1.7 dB  |
| Peaking | 8354 Hz  | 6.44 | -2.6 dB |
| Peaking | 12896 Hz | 2.82 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Jabra%20Elite%2025e/Jabra%20Elite%2025e.png)