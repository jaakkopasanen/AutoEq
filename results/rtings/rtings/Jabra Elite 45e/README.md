# Jabra Elite 45e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.5; 25 0.0; 28 -0.7; 31 -1.3; 34 -1.7; 37 -2.2; 41 -2.6; 45 -3.1; 49 -3.4; 54 -3.8; 60 -4.3; 66 -4.9; 72 -5.2; 79 -5.4; 87 -5.7; 96 -6.0; 106 -6.1; 116 -6.2; 128 -6.7; 141 -6.9; 155 -6.9; 170 -6.8; 187 -6.6; 206 -6.4; 227 -6.2; 249 -5.9; 274 -5.7; 302 -5.4; 332 -5.1; 365 -4.7; 402 -4.3; 442 -4.0; 486 -3.4; 535 -2.8; 588 -2.0; 647 -1.2; 712 -0.2; 783 0.5; 861 1.0; 947 0.6; 1042 -0.5; 1146 -1.3; 1261 -1.7; 1387 -2.0; 1526 -2.0; 1678 -1.4; 1846 -0.7; 2031 0.1; 2234 1.7; 2457 3.5; 2703 4.8; 2973 5.2; 3270 5.4; 3597 5.5; 3957 5.1; 4353 3.7; 4788 4.3; 5267 6.0; 5793 5.9; 6373 1.9; 7010 -1.0; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.1; 13660 -4.1; 15026 -5.6; 16529 -2.4; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 45e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 45e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 122 Hz   | 0.51 | -6.4 dB |
| Peaking | 313 Hz   | 1.2  | -2.5 dB |
| Peaking | 3225 Hz  | 1.63 | 7.4 dB  |
| Peaking | 5482 Hz  | 2.93 | 6.6 dB  |
| Peaking | 8200 Hz  | 0.15 | -2.0 dB |
| Peaking | 21 Hz    | 2.27 | 1.9 dB  |
| Peaking | 857 Hz   | 3.51 | 2.6 dB  |
| Peaking | 1446 Hz  | 2.54 | -1.9 dB |
| Peaking | 12235 Hz | 1.45 | 2.8 dB  |
| Peaking | 14701 Hz | 2.98 | -6.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Jabra%20Elite%2045e/Jabra%20Elite%2045e.png)