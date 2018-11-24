# Noontec Hammo Go

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.3; 41 4.5; 45 3.8; 49 3.5; 54 2.9; 60 1.9; 66 1.3; 72 0.7; 79 0.1; 87 -0.6; 96 -1.3; 106 -2.1; 116 -2.7; 128 -3.0; 141 -2.9; 155 -3.1; 170 -3.5; 187 -4.1; 206 -4.5; 227 -4.7; 249 -4.6; 274 -4.3; 302 -4.1; 332 -4.2; 365 -4.3; 402 -3.9; 442 -2.1; 486 -1.4; 535 -1.0; 588 -0.4; 647 0.3; 712 -0.3; 783 -0.1; 861 -0.5; 947 -0.5; 1042 0.4; 1146 1.5; 1261 2.1; 1387 2.8; 1526 3.1; 1678 3.5; 1846 3.7; 2031 3.3; 2234 2.9; 2457 2.2; 2703 2.0; 2973 1.3; 3270 -0.6; 3597 -4.1; 3957 -1.1; 4353 0.7; 4788 -2.0; 5267 -1.3; 5793 -2.1; 6373 -0.6; 7010 -1.8; 7711 -6.5; 8482 -9.4; 9330 -7.3; 10263 -3.5; 11289 -1.9; 12418 -0.1; 13660 0.0; 15026 0.0; 16529 -3.1; 18182 -5.4; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Hammo Go GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Hammo Go ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.7  | 6.5 dB   |
| Peaking | 168 Hz   | 0.85 | -4.1 dB  |
| Peaking | 332 Hz   | 2.02 | -3.1 dB  |
| Peaking | 8617 Hz  | 3.33 | -10.0 dB |
| Peaking | 17631 Hz | 3.51 | -6.5 dB  |
| Peaking | 941 Hz   | 3.53 | -1.7 dB  |
| Peaking | 1786 Hz  | 0.94 | 3.8 dB   |
| Peaking | 3613 Hz  | 8.37 | -5.5 dB  |
| Peaking | 5091 Hz  | 3.6  | -1.3 dB  |
| Peaking | 14318 Hz | 2.75 | 1.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Noontec%20Hammo%20Go/Noontec%20Hammo%20Go.png)