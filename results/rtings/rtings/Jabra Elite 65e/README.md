# Jabra Elite 65e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.2dB
GraphicEQ: 21 -7.5; 23 -7.8; 25 -8.0; 28 -8.2; 31 -8.4; 34 -8.4; 37 -8.5; 41 -8.5; 45 -8.4; 49 -8.3; 54 -8.2; 60 -8.0; 66 -8.1; 72 -7.9; 79 -7.7; 87 -7.7; 96 -7.4; 106 -7.2; 116 -6.8; 128 -6.7; 141 -6.3; 155 -5.8; 170 -5.5; 187 -5.0; 206 -4.6; 227 -4.4; 249 -4.2; 274 -4.0; 302 -3.8; 332 -3.8; 365 -3.7; 402 -3.6; 442 -3.3; 486 -3.0; 535 -2.5; 588 -2.0; 647 -1.5; 712 -1.0; 783 -0.5; 861 -0.2; 947 -0.0; 1042 0.0; 1146 0.1; 1261 -0.0; 1387 -0.9; 1526 -2.2; 1678 -3.2; 1846 -3.5; 2031 -3.2; 2234 -2.2; 2457 -1.0; 2703 -0.2; 2973 -0.3; 3270 -1.0; 3597 -2.0; 3957 -3.2; 4353 -4.1; 4788 -0.7; 5267 -0.2; 5793 0.1; 6373 -3.9; 7010 -7.4; 7711 -5.8; 8482 -5.8; 9330 -11.2; 10263 -15.0; 11289 -11.0; 12418 -5.5; 13660 -4.4; 15026 -5.7; 16529 -8.0; 18182 -8.1; 20000 -2.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 65e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-2**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 65e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 43 Hz    | 0.2  | -8.4 dB  |
| Peaking | 413 Hz   | 1.87 | -1.7 dB  |
| Peaking | 1866 Hz  | 3.09 | -3.6 dB  |
| Peaking | 10146 Hz | 2.06 | -14.2 dB |
| Peaking | 17661 Hz | 1.52 | -8.6 dB  |
| Peaking | 4186 Hz  | 5.28 | -4.1 dB  |
| Peaking | 5890 Hz  | 2.51 | 4.3 dB   |
| Peaking | 6823 Hz  | 4.52 | -6.8 dB  |
| Peaking | 8432 Hz  | 7.27 | 2.4 dB   |
| Peaking | 12837 Hz | 7.18 | 1.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Jabra%20Elite%2065e/Jabra%20Elite%2065e.png)