# Skullcandy Jib
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.0dB
GraphicEQ: 21 -4.5; 23 -4.7; 25 -4.9; 28 -5.2; 31 -5.3; 34 -5.4; 37 -5.5; 41 -5.5; 45 -5.6; 49 -5.6; 54 -5.7; 60 -6.0; 66 -6.3; 72 -6.5; 79 -6.8; 87 -7.1; 96 -7.4; 106 -7.8; 116 -8.2; 128 -8.6; 141 -8.8; 155 -8.8; 170 -8.8; 187 -8.6; 206 -8.3; 227 -7.8; 249 -7.3; 274 -6.8; 302 -6.2; 332 -5.7; 365 -5.1; 402 -4.6; 442 -4.0; 486 -3.3; 535 -2.6; 588 -1.8; 647 -1.0; 712 -0.1; 783 0.7; 861 0.9; 947 0.5; 1042 -0.4; 1146 -1.2; 1261 -1.6; 1387 -1.8; 1526 -1.9; 1678 -2.1; 1846 -2.3; 2031 -2.5; 2234 -2.1; 2457 -1.8; 2703 -2.5; 2973 -3.2; 3270 -3.0; 3597 -2.4; 3957 -2.1; 4353 -1.8; 4788 -1.6; 5267 -2.1; 5793 -2.4; 6373 -4.0; 7010 -2.2; 7711 0.1; 8482 -0.0; 9330 -1.8; 10263 -1.4; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -4.1; 18182 -8.1; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Jib GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-10**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Jib ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.27 | -5.0 dB |
| Peaking | 166 Hz   | 0.84 | -6.2 dB |
| Peaking | 331 Hz   | 1.59 | -2.6 dB |
| Peaking | 3445 Hz  | 0.62 | -2.7 dB |
| Peaking | 18468 Hz | 2.18 | -9.1 dB |
| Peaking | 833 Hz   | 4.18 | 2.4 dB  |
| Peaking | 4579 Hz  | 3.84 | 1.0 dB  |
| Peaking | 6486 Hz  | 4.78 | -2.7 dB |
| Peaking | 7814 Hz  | 6.38 | 1.9 dB  |
| Peaking | 14329 Hz | 3.29 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Jib/Skullcandy%20Jib.png)