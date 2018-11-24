# Jabra Elite 45e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.9; 25 0.3; 28 -0.5; 31 -1.2; 34 -1.8; 37 -2.3; 41 -2.8; 45 -3.3; 49 -3.8; 54 -4.2; 60 -4.6; 66 -5.0; 72 -5.2; 79 -5.3; 87 -5.4; 96 -5.5; 106 -5.6; 116 -5.7; 128 -6.2; 141 -6.4; 155 -6.3; 170 -6.1; 187 -6.1; 206 -5.9; 227 -5.7; 249 -5.4; 274 -5.0; 302 -4.6; 332 -4.1; 365 -3.7; 402 -3.3; 442 -2.8; 486 -2.2; 535 -1.6; 588 -0.9; 647 -0.1; 712 0.6; 783 1.0; 861 1.2; 947 0.7; 1042 -0.4; 1146 -1.1; 1261 -1.5; 1387 -2.0; 1526 -2.4; 1678 -1.7; 1846 -0.6; 2031 0.5; 2234 2.2; 2457 4.0; 2703 5.4; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.9; 4353 3.7; 4788 4.2; 5267 6.0; 5793 6.0; 6373 4.4; 7010 1.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.5; 15026 -2.3; 16529 -0.1; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 45e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 45e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 84 Hz    | 0.64 | -4.6 dB |
| Peaking | 223 Hz   | 0.84 | -4.5 dB |
| Peaking | 1588 Hz  | 2.67 | -3.6 dB |
| Peaking | 3175 Hz  | 1.4  | 6.5 dB  |
| Peaking | 5667 Hz  | 3.95 | 5.1 dB  |
| Peaking | 20 Hz    | 2.39 | 2.2 dB  |
| Peaking | 425 Hz   | 2.86 | -0.8 dB |
| Peaking | 789 Hz   | 3.3  | 2.0 dB  |
| Peaking | 14895 Hz | 4.24 | -2.6 dB |
| Peaking | 24000 Hz | 1.55 | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Jabra%20Elite%2045e/Jabra%20Elite%2045e.png)