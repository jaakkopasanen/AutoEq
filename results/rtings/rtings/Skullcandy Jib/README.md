# Skullcandy Jib

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.0dB
GraphicEQ: 21 -4.5; 23 -4.7; 25 -4.9; 28 -5.2; 31 -5.3; 34 -5.4; 37 -5.5; 41 -5.5; 45 -5.6; 49 -5.6; 54 -5.7; 60 -6.0; 66 -6.3; 72 -6.5; 79 -6.8; 87 -7.1; 96 -7.4; 106 -7.8; 116 -8.2; 128 -8.6; 141 -8.8; 155 -8.8; 170 -8.8; 187 -8.6; 206 -8.3; 227 -7.8; 249 -7.3; 274 -6.8; 302 -6.2; 332 -5.7; 365 -5.1; 402 -4.6; 442 -4.0; 486 -3.3; 535 -2.6; 588 -1.8; 647 -1.0; 712 -0.1; 783 0.7; 861 0.9; 947 0.5; 1042 -0.4; 1146 -1.2; 1261 -1.6; 1387 -1.8; 1526 -1.9; 1678 -2.1; 1846 -2.3; 2031 -2.5; 2234 -2.1; 2457 -1.8; 2703 -2.3; 2973 -2.7; 3270 -2.3; 3597 -1.4; 3957 -0.8; 4353 -0.5; 4788 0.2; 5267 0.5; 5793 0.0; 6373 -2.8; 7010 -1.3; 7711 0.3; 8482 0.0; 9330 -3.1; 10263 -3.2; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.3; 18182 -3.8; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Jib GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-10**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Jib ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 54 Hz    | 0.26 | -4.9 dB |
| Peaking | 193 Hz   | 0.68 | -6.0 dB |
| Peaking | 2461 Hz  | 1.11 | -2.4 dB |
| Peaking | 17982 Hz | 2.95 | -4.3 dB |
| Peaking | 418 Hz   | 2.49 | -0.9 dB |
| Peaking | 814 Hz   | 3.43 | 2.5 dB  |
| Peaking | 6545 Hz  | 6.82 | -4.1 dB |
| Peaking | 8380 Hz  | 0.97 | 2.0 dB  |
| Peaking | 9772 Hz  | 4.57 | -5.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Skullcandy%20Jib/Skullcandy%20Jib.png)