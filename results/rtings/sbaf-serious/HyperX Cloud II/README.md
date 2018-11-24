# HyperX Cloud II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.3; 23 -2.7; 25 -3.1; 28 -3.7; 31 -4.2; 34 -4.6; 37 -4.8; 41 -5.0; 45 -5.1; 49 -5.1; 54 -5.0; 60 -5.1; 66 -5.1; 72 -5.1; 79 -5.1; 87 -5.3; 96 -5.6; 106 -5.9; 116 -6.2; 128 -6.3; 141 -6.0; 155 -5.7; 170 -5.3; 187 -4.8; 206 -4.0; 227 -3.2; 249 -2.4; 274 -1.9; 302 -1.7; 332 -1.6; 365 -1.7; 402 -1.6; 442 -1.5; 486 -1.5; 535 -1.6; 588 -1.6; 647 -1.4; 712 -1.4; 783 -1.4; 861 -1.3; 947 -0.5; 1042 0.2; 1146 0.0; 1261 -0.6; 1387 -1.5; 1526 -2.5; 1678 -3.5; 1846 -4.1; 2031 -4.9; 2234 -5.0; 2457 -3.7; 2703 -2.1; 2973 -0.6; 3270 1.0; 3597 4.4; 3957 6.0; 4353 5.4; 4788 -1.9; 5267 -0.2; 5793 0.9; 6373 -1.0; 7010 -2.3; 7711 -4.4; 8482 -8.7; 9330 -9.9; 10263 -3.7; 11289 0.0; 12418 0.0; 13660 -0.6; 15026 -2.8; 16529 -0.5; 18182 0.0; 20000 -1.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.77 | -4.0 dB  |
| Peaking | 130 Hz   | 0.7  | -5.5 dB  |
| Peaking | 2098 Hz  | 1.88 | -5.4 dB  |
| Peaking | 3912 Hz  | 4.27 | 7.9 dB   |
| Peaking | 8938 Hz  | 3.78 | -11.1 dB |
| Peaking | 798 Hz   | 1.28 | -1.2 dB  |
| Peaking | 1080 Hz  | 3.43 | 1.9 dB   |
| Peaking | 9870 Hz  | 7.84 | -3.1 dB  |
| Peaking | 10983 Hz | 3.16 | 2.8 dB   |
| Peaking | 15036 Hz | 4.62 | -3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/HyperX%20Cloud%20II/HyperX%20Cloud%20II.png)