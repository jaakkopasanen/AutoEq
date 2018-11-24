# Jabra Elite Sport

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.3; 23 -3.4; 25 -3.5; 28 -3.6; 31 -3.7; 34 -3.9; 37 -4.0; 41 -4.2; 45 -4.3; 49 -4.4; 54 -4.6; 60 -4.9; 66 -5.2; 72 -5.3; 79 -5.4; 87 -5.7; 96 -6.0; 106 -6.4; 116 -6.8; 128 -7.2; 141 -7.4; 155 -7.4; 170 -7.3; 187 -7.2; 206 -6.9; 227 -6.5; 249 -5.7; 274 -4.6; 302 -3.3; 332 -2.3; 365 -1.6; 402 -1.2; 442 -0.9; 486 -0.7; 535 -0.4; 588 0.0; 647 0.5; 712 0.8; 783 0.6; 861 0.4; 947 0.2; 1042 -0.1; 1146 0.0; 1261 0.5; 1387 0.8; 1526 0.5; 1678 -0.0; 1846 -0.5; 2031 -0.9; 2234 -0.5; 2457 0.2; 2703 1.2; 2973 2.6; 3270 4.2; 3597 5.1; 3957 4.6; 4353 3.5; 4788 4.5; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.8; 8482 -2.4; 9330 -3.3; 10263 -4.0; 11289 -1.5; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite Sport GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite Sport ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 55 Hz   | 0.38 | -4.3 dB |
| Peaking | 174 Hz  | 1.05 | -5.9 dB |
| Peaking | 3561 Hz | 3.49 | 4.3 dB  |
| Peaking | 5808 Hz | 2.01 | 7.0 dB  |
| Peaking | 9252 Hz | 2.07 | -5.1 dB |
| Peaking | 14 Hz   | 1.75 | -0.8 dB |
| Peaking | 249 Hz  | 5.48 | -1.1 dB |
| Peaking | 653 Hz  | 1.46 | 1.0 dB  |
| Peaking | 1929 Hz | 1.21 | 1.4 dB  |
| Peaking | 2102 Hz | 2.48 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Jabra%20Elite%20Sport/Jabra%20Elite%20Sport.png)