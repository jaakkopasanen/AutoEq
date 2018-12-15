# Noontec Hammo Go

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.3; 41 4.5; 45 3.8; 49 3.5; 54 2.9; 60 1.9; 66 1.3; 72 0.7; 79 0.1; 87 -0.6; 96 -1.3; 106 -2.1; 116 -2.7; 128 -3.0; 141 -2.9; 155 -3.1; 170 -3.5; 187 -4.1; 206 -4.5; 227 -4.7; 249 -4.6; 274 -4.3; 302 -4.1; 332 -4.2; 365 -4.3; 402 -3.9; 442 -2.1; 486 -1.4; 535 -1.0; 588 -0.4; 647 0.3; 712 -0.3; 783 -0.1; 861 -0.5; 947 -0.5; 1042 0.4; 1146 1.5; 1261 2.1; 1387 2.8; 1526 3.1; 1678 3.5; 1846 3.7; 2031 3.3; 2234 2.9; 2457 2.2; 2703 1.7; 2973 0.8; 3270 -1.3; 3597 -5.2; 3957 -2.3; 4353 -0.6; 4788 -3.8; 5267 -3.9; 5793 -4.5; 6373 -1.8; 7010 -2.7; 7711 -7.9; 8482 -10.1; 9330 -5.9; 10263 -1.8; 11289 -2.7; 12418 -2.7; 13660 -0.1; 15026 -0.2; 16529 -6.1; 18182 -9.7; 20000 0.0
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
| Peaking | 27 Hz    | 0.7  | 6.5 dB   |
| Peaking | 166 Hz   | 0.84 | -4.1 dB  |
| Peaking | 330 Hz   | 1.97 | -3.1 dB  |
| Peaking | 8300 Hz  | 2.74 | -9.8 dB  |
| Peaking | 17948 Hz | 2.54 | -11.0 dB |
| Peaking | 1819 Hz  | 1.4  | 3.8 dB   |
| Peaking | 3631 Hz  | 7.81 | -5.9 dB  |
| Peaking | 5199 Hz  | 0.45 | 0.8 dB   |
| Peaking | 5537 Hz  | 2.25 | -4.5 dB  |
| Peaking | 6649 Hz  | 6.86 | 4.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Noontec%20Hammo%20Go/Noontec%20Hammo%20Go.png)