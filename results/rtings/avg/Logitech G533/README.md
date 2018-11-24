# Logitech G533

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 21 -3.5; 23 -3.7; 25 -3.9; 28 -4.2; 31 -4.4; 34 -4.4; 37 -4.4; 41 -4.2; 45 -4.1; 49 -4.0; 54 -3.9; 60 -3.9; 66 -4.0; 72 -4.0; 79 -4.1; 87 -4.3; 96 -4.5; 106 -4.7; 116 -4.8; 128 -4.8; 141 -4.7; 155 -4.7; 170 -4.6; 187 -4.5; 206 -4.2; 227 -4.0; 249 -4.0; 274 -4.3; 302 -4.7; 332 -4.7; 365 -4.2; 402 -3.4; 442 -2.8; 486 -2.4; 535 -1.7; 588 -1.1; 647 -0.8; 712 -0.3; 783 0.7; 861 1.1; 947 0.3; 1042 -0.2; 1146 -0.5; 1261 -0.1; 1387 1.1; 1526 2.2; 1678 1.6; 1846 0.6; 2031 -0.2; 2234 -0.0; 2457 0.5; 2703 -2.5; 2973 -2.2; 3270 -1.7; 3597 -2.8; 3957 -3.8; 4353 -4.5; 4788 -2.5; 5267 -0.7; 5793 -1.2; 6373 -3.2; 7010 -2.8; 7711 -2.4; 8482 -5.1; 9330 -5.0; 10263 -0.6; 11289 -0.4; 12418 -5.1; 13660 -7.5; 15026 -5.5; 16529 -5.5; 18182 -10.0; 20000 -15.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G533 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-24**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G533 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.39 | -3.9 dB  |
| Peaking | 145 Hz   | 0.83 | -3.6 dB  |
| Peaking | 335 Hz   | 1.81 | -3.5 dB  |
| Peaking | 4097 Hz  | 2.48 | -3.8 dB  |
| Peaking | 21125 Hz | 0.39 | -15.4 dB |
| Peaking | 845 Hz   | 4.28 | 1.3 dB   |
| Peaking | 1582 Hz  | 4.21 | 2.5 dB   |
| Peaking | 8934 Hz  | 3.52 | -4.1 dB  |
| Peaking | 10688 Hz | 5.33 | 4.6 dB   |
| Peaking | 15483 Hz | 2.52 | 0.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G533/Logitech%20G533.png)