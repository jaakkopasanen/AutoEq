# Xiaomi Crystal

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.3dB
GraphicEQ: 21 -7.1; 23 -7.3; 25 -7.5; 28 -7.8; 31 -8.1; 34 -8.2; 37 -8.3; 41 -8.5; 45 -8.6; 49 -8.7; 54 -8.9; 60 -9.1; 66 -9.2; 72 -9.4; 79 -9.6; 87 -9.7; 96 -9.9; 106 -9.8; 116 -9.7; 128 -9.6; 141 -9.5; 155 -9.3; 170 -9.0; 187 -8.6; 206 -8.2; 227 -7.6; 249 -7.2; 274 -6.6; 302 -6.0; 332 -5.4; 365 -4.8; 402 -4.1; 442 -3.3; 486 -2.8; 535 -2.2; 588 -1.4; 647 -0.8; 712 -0.4; 783 0.1; 861 0.1; 947 0.1; 1042 0.0; 1146 -0.2; 1261 -0.3; 1387 -0.5; 1526 -0.7; 1678 -0.9; 1846 -2.2; 2031 -2.7; 2234 -2.7; 2457 -2.2; 2703 -2.1; 2973 -1.5; 3270 -0.9; 3597 -0.4; 3957 -1.0; 4353 -3.4; 4788 -4.7; 5267 -5.8; 5793 -7.4; 6373 -6.8; 7010 -4.4; 7711 -3.4; 8482 -4.4; 9330 -5.9; 10263 -4.9; 11289 -0.8; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Xiaomi Crystal GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-2**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Crystal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.29 | -7.5 dB |
| Peaking | 137 Hz   | 0.66 | -5.5 dB |
| Peaking | 283 Hz   | 1.17 | -2.8 dB |
| Peaking | 5825 Hz  | 1.86 | -7.1 dB |
| Peaking | 9563 Hz  | 4.33 | -5.3 dB |
| Peaking | 867 Hz   | 1.98 | 1.1 dB  |
| Peaking | 2173 Hz  | 2.26 | -2.4 dB |
| Peaking | 3655 Hz  | 5.75 | 1.8 dB  |
| Peaking | 12266 Hz | 5.02 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Crystal/Xiaomi%20Crystal.png)