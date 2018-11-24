# Panasonic RP-HC800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.4dB
GraphicEQ: 21 -13.3; 23 -13.1; 25 -13.0; 28 -12.9; 31 -12.8; 34 -12.6; 37 -12.5; 41 -12.3; 45 -12.2; 49 -12.0; 54 -11.9; 60 -11.8; 66 -11.9; 72 -11.9; 79 -12.0; 87 -12.2; 96 -12.3; 106 -12.5; 116 -12.7; 128 -12.9; 141 -13.0; 155 -13.1; 170 -13.1; 187 -13.0; 206 -12.8; 227 -12.5; 249 -12.2; 274 -12.0; 302 -11.8; 332 -11.5; 365 -11.0; 402 -10.6; 442 -10.1; 486 -9.4; 535 -8.2; 588 -6.8; 647 -4.5; 712 -1.8; 783 -0.1; 861 0.0; 947 0.2; 1042 -0.8; 1146 -2.1; 1261 -3.0; 1387 -2.4; 1526 -2.0; 1678 -2.1; 1846 -3.8; 2031 -4.7; 2234 -6.2; 2457 -6.3; 2703 -3.2; 2973 -0.8; 3270 -2.1; 3597 -2.7; 3957 -3.7; 4353 -6.3; 4788 -6.5; 5267 -5.3; 5793 -8.3; 6373 -13.2; 7010 -9.1; 7711 -5.8; 8482 -8.8; 9330 -12.4; 10263 -12.6; 11289 -11.5; 12418 -9.3; 13660 -7.7; 15026 -9.0; 16529 -9.1; 18182 -6.7; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-3**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.11 | -12.6 dB |
| Peaking | 208 Hz   | 0.75 | -7.5 dB  |
| Peaking | 426 Hz   | 1.83 | -5.7 dB  |
| Peaking | 10005 Hz | 0.41 | -10.5 dB |
| Peaking | 21874 Hz | 0.68 | -10.2 dB |
| Peaking | 842 Hz   | 3.98 | 3.3 dB   |
| Peaking | 2429 Hz  | 2.36 | -7.6 dB  |
| Peaking | 2902 Hz  | 2.3  | 6.7 dB   |
| Peaking | 6415 Hz  | 8.64 | -5.7 dB  |
| Peaking | 7694 Hz  | 7.61 | 5.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Panasonic%20RP-HC800/Panasonic%20RP-HC800.png)