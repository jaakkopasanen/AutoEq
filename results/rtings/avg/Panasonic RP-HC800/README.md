# Panasonic RP-HC800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.4dB
GraphicEQ: 21 -13.3; 23 -13.1; 25 -13.0; 28 -12.9; 31 -12.8; 34 -12.6; 37 -12.5; 41 -12.3; 45 -12.2; 49 -12.0; 54 -11.9; 60 -11.8; 66 -11.9; 72 -11.9; 79 -12.0; 87 -12.2; 96 -12.3; 106 -12.5; 116 -12.7; 128 -12.9; 141 -13.0; 155 -13.1; 170 -13.1; 187 -13.0; 206 -12.8; 227 -12.5; 249 -12.2; 274 -12.0; 302 -11.8; 332 -11.5; 365 -11.0; 402 -10.6; 442 -10.1; 486 -9.4; 535 -8.2; 588 -6.8; 647 -4.5; 712 -1.8; 783 -0.1; 861 0.0; 947 0.2; 1042 -0.8; 1146 -2.1; 1261 -3.0; 1387 -2.4; 1526 -2.0; 1678 -2.1; 1846 -3.8; 2031 -4.7; 2234 -6.2; 2457 -6.3; 2703 -3.4; 2973 -1.3; 3270 -2.8; 3597 -3.8; 3957 -5.0; 4353 -7.6; 4788 -8.3; 5267 -7.9; 5793 -10.8; 6373 -14.5; 7010 -9.7; 7711 -6.2; 8482 -7.9; 9330 -9.8; 10263 -10.4; 11289 -12.4; 12418 -12.6; 13660 -10.9; 15026 -11.6; 16529 -12.1; 18182 -11.0; 20000 -14.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP-HC800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-3**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP-HC800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.11 | -12.6 dB |
| Peaking | 207 Hz   | 0.76 | -7.5 dB  |
| Peaking | 424 Hz   | 1.84 | -5.8 dB  |
| Peaking | 6247 Hz  | 6.79 | -6.7 dB  |
| Peaking | 20130 Hz | 0.08 | -12.0 dB |
| Peaking | 578 Hz   | 4.11 | -2.3 dB  |
| Peaking | 819 Hz   | 2.59 | 3.5 dB   |
| Peaking | 2467 Hz  | 2.3  | -5.4 dB  |
| Peaking | 2924 Hz  | 3.52 | 6.2 dB   |
| Peaking | 7847 Hz  | 6.97 | 4.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Panasonic%20RP-HC800/Panasonic%20RP-HC800.png)