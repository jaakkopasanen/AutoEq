# MEE audio M6 PRO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.4; 28 1.2; 31 1.0; 34 0.8; 37 0.7; 41 0.6; 45 0.6; 49 0.5; 54 0.3; 60 -0.2; 66 -0.5; 72 -0.8; 79 -1.2; 87 -1.6; 96 -2.0; 106 -2.6; 116 -3.0; 128 -3.4; 141 -3.7; 155 -3.9; 170 -3.9; 187 -3.9; 206 -3.7; 227 -3.5; 249 -3.3; 274 -2.9; 302 -2.5; 332 -1.9; 365 -1.4; 402 -1.0; 442 -0.7; 486 -0.3; 535 0.3; 588 0.8; 647 1.1; 712 1.3; 783 1.4; 861 1.0; 947 0.3; 1042 -0.3; 1146 -1.4; 1261 -1.9; 1387 -2.3; 1526 -2.9; 1678 -3.7; 1846 -4.6; 2031 -5.5; 2234 -6.0; 2457 -6.8; 2703 -8.5; 2973 -9.0; 3270 -8.1; 3597 -7.7; 3957 -8.4; 4353 -10.8; 4788 -13.9; 5267 -15.2; 5793 -8.6; 6373 -4.8; 7010 -2.8; 7711 -3.4; 8482 -3.9; 9330 -1.4; 10263 0.0; 11289 0.0; 12418 -0.3; 13660 -2.2; 15026 -1.3; 16529 -1.8; 18182 -2.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M6 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-21**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M6 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 171 Hz   | 1.01 | -4.3 dB  |
| Peaking | 2767 Hz  | 1.28 | -7.5 dB  |
| Peaking | 5050 Hz  | 2.99 | -13.9 dB |
| Peaking | 13964 Hz | 4.76 | -1.7 dB  |
| Peaking | 17774 Hz | 2.46 | -2.8 dB  |
| Peaking | 20 Hz    | 0.99 | 1.8 dB   |
| Peaking | 737 Hz   | 2.56 | 2.4 dB   |
| Peaking | 6986 Hz  | 3.58 | 2.7 dB   |
| Peaking | 8482 Hz  | 2.07 | -4.2 dB  |
| Peaking | 9895 Hz  | 2.52 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/MEE%20audio%20M6%20PRO/MEE%20audio%20M6%20PRO.png)